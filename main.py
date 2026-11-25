#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes a single commit message for a bug fix that made everything
worse to /output/entry.txt. The message is at most 100 characters,
as the gate requires.
"""

import os
import sys

# The commit message. The fix: logins kept failing, so the engineer
# "fixed" it by removing login entirely. No more failed logins.
ENTRY = "fix(auth): removed login to stop the failed logins"

MAX_CHARS = 100
OUTPUT_PATH = "/output/entry.txt"


def check_entry(text):
    """Make sure the entry passes the gate before writing it out."""
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    return text


def main():
    entry = check_entry(ENTRY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)
    print("wrote %d chars to %s" % (len(entry), OUTPUT_PATH))
    print(entry)


if __name__ == "__main__":
    sys.exit(main())

