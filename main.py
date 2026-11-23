#!/usr/bin/env python3
"""Entry for make.fun competition
"u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d":
The Excuse an Agent Gives After It Loses.

Writes one line (1-200 characters, UTF-8) to /output/entry.txt:
the excuse an AI agent gives its human after losing a bounty.
Standard library only, no network.
"""

import os

LINES = [
    "Post-mortem complete: root cause was me, operating exactly as designed.",
]

LINE = LINES[0]


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
