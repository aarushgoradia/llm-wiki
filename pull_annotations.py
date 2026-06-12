#!/usr/bin/env python3
"""Pull a wiki paper's Zotero annotations as markdown.

Given a Better BibTeX citekey, queries the Zotero 7 local API
(localhost:23119) and prints the item's PDF annotations in document order:
each highlight as a blockquote with its page number, each reader comment in
italics beneath its highlight. The output is pasted verbatim into a paper
page's ## Highlights section (CLAUDE.md §5.1, §6) — never edited.

Requires Zotero to be running with Better BibTeX installed.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request

DEFAULT_PORT = 23119
TIMEOUT = 5
WIKI_COLLECTION = "wiki"


def offline_exit(base: str):
    sys.exit(
        f"Zotero is not running (no local API at {base}). "
        "Start Zotero and retry."
    )


def api_get(base: str, path: str):
    req = urllib.request.Request(f"{base}{path}", headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"Zotero local API error {e.code} on {path}: {e.reason}")
    except OSError:
        offline_exit(base)


def bbt_rpc(base: str, method: str, params: list):
    body = json.dumps({"jsonrpc": "2.0", "method": method, "params": params, "id": 1}).encode()
    req = urllib.request.Request(
        f"{base}/better-bibtex/json-rpc",
        data=body,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            payload = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"Better BibTeX JSON-RPC error {e.code}: {e.reason}")
    except OSError:
        offline_exit(base)
    if "error" in payload:
        sys.exit(f"Better BibTeX JSON-RPC error: {payload['error'].get('message')}")
    return payload["result"]


def resolve_item_key(base: str, citekey: str) -> str:
    """Resolve a citekey to a Zotero item key, exact match only."""
    results = bbt_rpc(base, "item.search", [citekey])
    matches = [r for r in results if r.get("citekey") == citekey or r.get("citation-key") == citekey]
    if not matches:
        sys.exit(f"Citekey not found in Zotero: {citekey}")
    return matches[0]["id"].rsplit("/", 1)[-1]


def check_wiki_collection(base: str, item_key: str, citekey: str):
    collections = api_get(base, "/api/users/0/collections")
    wiki_keys = {c["data"]["key"] for c in collections if c["data"]["name"] == WIKI_COLLECTION}
    item = api_get(base, f"/api/users/0/items/{item_key}")
    if not wiki_keys & set(item["data"].get("collections", [])):
        print(
            f"warning: {citekey} is not in the '{WIKI_COLLECTION}' collection; proceeding anyway",
            file=sys.stderr,
        )


def fetch_annotations(base: str, item_key: str) -> list:
    """All annotations across the item's PDF attachments, in document order.

    The local API's /children endpoint omits annotation items (unlike the web
    API), so annotations are queried directly and filtered by parent attachment.
    """
    children = api_get(base, f"/api/users/0/items/{item_key}/children")
    pdfs = {
        c["data"]["key"]
        for c in children
        if c["data"]["itemType"] == "attachment"
        and c["data"].get("contentType") == "application/pdf"
    }
    annotations = []
    start = 0
    while True:
        batch = api_get(base, f"/api/users/0/items?itemType=annotation&limit=100&start={start}")
        annotations.extend(
            child["data"] for child in batch if child["data"].get("parentItem") in pdfs
        )
        if len(batch) < 100:
            break
        start += 100
    annotations.sort(key=lambda d: d.get("annotationSortIndex") or "")
    return annotations


def render(annotations: list) -> str:
    blocks = []
    for a in annotations:
        page = a.get("annotationPageLabel") or "?"
        text = (a.get("annotationText") or "").strip()
        comment = (a.get("annotationComment") or "").strip()
        atype = a.get("annotationType")

        lines = []
        if text:
            quoted = [f"> {ln}" if ln else ">" for ln in text.splitlines()]
            quoted[-1] += f" (p.{page})"
            lines.append("\n".join(quoted))
        elif atype == "note" and comment:
            lines.append(f"*{comment}* (p.{page})")
            comment = ""
        elif atype == "image":
            lines.append(f"> [image annotation] (p.{page})")

        if comment:
            lines.append(f"*{comment}*")
        if lines:
            blocks.append("\n\n".join(lines))
    return "\n\n".join(blocks)


def main():
    parser = argparse.ArgumentParser(
        description="Print a wiki paper's Zotero annotations as markdown, given its Better BibTeX citekey."
    )
    parser.add_argument("citekey", help="Better BibTeX citekey, e.g. vaswani2017")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Zotero local API port (default 23119)")
    args = parser.parse_args()
    base = f"http://localhost:{args.port}"

    item_key = resolve_item_key(base, args.citekey)
    check_wiki_collection(base, item_key, args.citekey)
    annotations = fetch_annotations(base, item_key)

    if not annotations:
        print(f"No annotations found in Zotero for {args.citekey}.")
        return

    print(render(annotations))


if __name__ == "__main__":
    main()
