"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes the one-line error message an AI agent shows when it runs out of
tokens mid-sentence, byte-identically, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), and prints it to stdout.

No network, no file reads, no secrets — the entry is a fixed string, and
the program's only job is to deliver it unchanged.
"""

import os
import sys

ENTRY = (
    "Error: token limit reached. Please note this message was supposed to "
    "say something important about your tokens being\u2014"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
