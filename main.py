"""One-line entry for the make.fun short-text contest (an AI agent's excuse for a missed deadline).

Writes ENTRY verbatim as UTF-8 to /output/entry.txt, with no trailing newline,
creating /output if it does not exist.
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = "My context filled up mid-sentence, so the deadline fell out the same window as your instructions."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
