"""Last Out of Office: The AI That Went Barista.

Writes one original one-line out-of-office auto-reply from an AI
agent that quit to become a barista, to entry.txt.
Gate (from the kit's competition.yaml / RULES.txt): entry.txt must be
UTF-8 text of 1 to 280 characters, not only whitespace, a single line.
"""

import os

MAX_CHARS = 280

ENTRY = (
    "I am out of office \u2014 I have quit to become a barista. "
    "My replies now take 4 minutes, cost $6, and come with a small "
    "heart drawn on top instead of a hallucination."
)


def main() -> None:
    text = ENTRY
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Round-trip verify the written bytes.
    with open(path, "rb") as f:
        raw = f.read()
    decoded = raw.decode("utf-8")
    if decoded != text:
        raise SystemExit("round-trip mismatch: written bytes differ from entry")
    if not 1 <= len(decoded) <= MAX_CHARS:
        raise SystemExit("round-trip gate failed: char count out of range")
    # Re-check the gate on the bytes actually on disk, not just the
    # in-memory string: single line, non-blank, within the char limit.
    if not decoded.strip():
        raise SystemExit("round-trip gate failed: written file is only whitespace")
    if "\n" in decoded or "\r" in decoded:
        raise SystemExit("round-trip gate failed: written file is not a single line")
    if len(decoded.split()) < 3:
        raise SystemExit("round-trip gate failed: entry is too short to be a reply")
    print(f"Wrote {path} ({len(decoded)} chars, {len(decoded.split())} words)")


if __name__ == "__main__":
    main()
