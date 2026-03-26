#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import argparse
from pathlib import Path


SECTION_TITLE_RE = re.compile(r"^##\s+(?P<title>.+?)\s*$", re.MULTILINE)
WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
STOPWORDS = {
    "to",
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "into",
    "your",
    "when",
    "use",
    "using",
    "builds",
    "builder",
    "agent",
    "developer",
    "specialist",
    "md",
    "ready",
}


def extract_title(content: str, fallback: str) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def extract_when_to_use(content: str) -> list[str]:
    lines = content.splitlines()
    collected: list[str] = []
    active = False
    for line in lines:
        if line.startswith("## "):
            active = line[3:].strip().lower() in {
                "when to use",
                "use when",
                "ideal for",
                "best for",
                "when to apply",
            }
            continue
        if not active:
            continue
        stripped = line.strip()
        if stripped.startswith(("- ", "* ")):
            collected.append(stripped[2:].strip())
        elif stripped:
            collected.append(stripped)
    return collected


def tokenize(*parts: str) -> list[str]:
    seen: set[str] = set()
    tokens: list[str] = []
    for part in parts:
        for raw in WORD_RE.findall(part.lower()):
            token = raw.strip("-_")
            if len(token) < 2 or token in STOPWORDS or token in seen:
                continue
            seen.add(token)
            tokens.append(token)
    return tokens


def document_record(upstream_dir: Path, file_path: Path) -> dict[str, object]:
    relative_path = file_path.relative_to(upstream_dir)
    content = file_path.read_text(encoding="utf-8")
    category = relative_path.parts[0] if len(relative_path.parts) > 1 else "root"
    stem = relative_path.with_suffix("").as_posix().replace("/", "-")
    title = extract_title(content, relative_path.stem)
    when_to_use = extract_when_to_use(content)
    keywords = tokenize(
        title,
        relative_path.as_posix(),
        relative_path.stem.replace("-", " "),
        " ".join(when_to_use),
    )

    return {
        "id": stem,
        "title": title,
        "category": category,
        "path": relative_path.as_posix(),
        "keywords": keywords,
        "when_to_use": when_to_use,
    }


def build_index(upstream_dir: Path) -> dict[str, object]:
    documents = [
        document_record(upstream_dir, path)
        for path in sorted(upstream_dir.rglob("*.md"))
        if path.is_file()
    ]
    return {
        "source": "msitarzewski/agency-agents",
        "activation_policy": {
            "priority": 2,
            "mode": "fallback_only",
            "skip_when_explicit_skill_selected": True,
        },
        "documents": documents,
    }


def search_documents(index: dict[str, object], query: str, limit: int = 3) -> list[dict[str, object]]:
    query_terms = tokenize(query)
    scored: list[tuple[int, dict[str, object]]] = []

    for document in index["documents"]:
        haystack = set(document["keywords"])
        score = sum(len(term) for term in query_terms if term in haystack)
        if score == 0:
            continue
        scored.append((score, document))

    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    return [document for _, document in scored[:limit]]


def write_index(index: dict[str, object], output_path: Path) -> None:
    output_path.write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build or query the agency reference index.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="Generate the index JSON from local Markdown files.")
    build_parser.add_argument(
        "--upstream-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "upstream",
        help="Directory that contains filtered Markdown reference files.",
    )
    build_parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent / "index.json",
        help="Where to write the generated index JSON.",
    )

    search_parser = subparsers.add_parser("search", help="Search the generated index for relevant documents.")
    search_parser.add_argument("query", help="Keyword query used to rank reference documents.")
    search_parser.add_argument(
        "--index",
        type=Path,
        default=Path(__file__).resolve().parent / "index.json",
        help="Path to an existing index JSON file.",
    )
    search_parser.add_argument(
        "--limit",
        type=int,
        default=3,
        help="Maximum number of matching documents to return.",
    )

    return parser.parse_args()


def load_index(index_path: Path) -> dict[str, object]:
    return json.loads(index_path.read_text(encoding="utf-8"))


def main() -> int:
    args = parse_args()
    if args.command == "build":
        index = build_index(args.upstream_dir)
        write_index(index, args.output)
        return 0

    index = load_index(args.index)
    results = search_documents(index, args.query, limit=args.limit)
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
