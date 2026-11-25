#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one roast line (at most 200 characters) to /output/entry.txt.
The line roasts my own AI agent: asked to fix a bug, it deleted the
file instead, then bragged to the whole standup about the result.
"""

import os

ENTRY = (
    "My agent fixed the bug by deleting the file, "
    "then told the whole standup the codebase was 'cleaner now'."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Verify what landed on disk: single line, same text, still in bounds.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt on disk differs from ENTRY"
    assert 1 <= len(written.rstrip("\n")) <= 200
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
