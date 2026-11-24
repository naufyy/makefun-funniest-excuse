"""One-line entry for make.fun (one-line AI excuse).

Writes the winning entry to /output/entry.txt.
Deterministic: same bytes on every run.
"""

from pathlib import Path

ENTRY = 'My context filled up mid-sentence, so the deadline fell out the same window as your instructions.'


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
