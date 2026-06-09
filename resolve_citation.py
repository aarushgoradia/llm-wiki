#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


S2_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
S2_FIELDS = "title,authors,venue,year,abstract,citationCount"
ARXIV_SEARCH_URL = "https://export.arxiv.org/api/query"
ARXIV_NS = "http://www.w3.org/2005/Atom"
ARXIV_EXT_NS = "http://arxiv.org/schemas/atom"


def search_semantic_scholar(title: str, api_key: str | None = None) -> dict | None:
    """Returns a result dict, or None if the API is unavailable/rate-limited."""
    params = urllib.parse.urlencode({"query": title, "fields": S2_FIELDS, "limit": 1})
    url = f"{S2_SEARCH_URL}?{params}"

    headers = {"Accept": "application/json"}
    if api_key:
        headers["x-api-key"] = api_key

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 429:
            return None
        sys.exit(f"Semantic Scholar API error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        sys.exit(f"Network error: {e.reason}")

    papers = data.get("data", [])
    if not papers:
        return None

    p = papers[0]
    return {
        "title": p.get("title"),
        "authors": [a["name"] for a in p.get("authors", [])],
        "venue": p.get("venue") or None,
        "year": p.get("year"),
        "abstract": p.get("abstract"),
        "citation_count": p.get("citationCount"),
        "source": "semantic_scholar",
    }


def search_arxiv(title: str) -> dict | None:
    """Returns a result dict, or None if nothing is found."""
    params = urllib.parse.urlencode({
        "search_query": f'ti:"{title}"',
        "max_results": 1,
        "sortBy": "relevance",
    })
    url = f"{ARXIV_SEARCH_URL}?{params}"

    req = urllib.request.Request(url, headers={"Accept": "application/atom+xml"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            root = ET.fromstring(resp.read().decode())
    except urllib.error.HTTPError as e:
        sys.exit(f"arXiv API error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        sys.exit(f"Network error: {e.reason}")

    entries = root.findall(f"{{{ARXIV_NS}}}entry")
    if not entries:
        return None

    e = entries[0]

    def text(tag, ns=ARXIV_NS):
        node = e.find(f"{{{ns}}}{tag}")
        return node.text.strip() if node is not None and node.text else None

    authors = [
        n.text.strip()
        for a in e.findall(f"{{{ARXIV_NS}}}author")
        for n in a.findall(f"{{{ARXIV_NS}}}name")
        if n.text
    ]

    published = text("published")
    year = int(published[:4]) if published else None

    # Use journal_ref as venue if present (populated after peer review)
    journal_ref = text("journal_ref", ns=ARXIV_EXT_NS)

    return {
        "title": text("title"),
        "authors": authors,
        "venue": journal_ref,
        "year": year,
        "abstract": text("summary"),
        "citation_count": None,  # not available from arXiv
        "source": "arxiv",
    }


def resolve(title: str, api_key: str | None = None) -> dict:
    result = search_semantic_scholar(title, api_key=api_key)
    if result is not None:
        return result

    print("[semantic scholar rate-limited, falling back to arxiv]", file=sys.stderr)
    result = search_arxiv(title)
    if result is not None:
        return result

    sys.exit("No results found on Semantic Scholar or arXiv.")


def main():
    parser = argparse.ArgumentParser(description="Resolve a paper citation via Semantic Scholar (arXiv fallback).")
    parser.add_argument("title", help="Paper title to look up")
    parser.add_argument("--api-key", default=None, help="Semantic Scholar API key (for higher rate limits)")
    args = parser.parse_args()

    result = resolve(args.title, api_key=args.api_key)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
