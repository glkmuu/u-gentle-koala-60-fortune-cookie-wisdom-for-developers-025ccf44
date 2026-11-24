#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — entry program.

Writes one original fortune-cookie line for a developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Stdlib only,
no network, no randomness, no clock: the output is fixed.
"""

import os
import sys

ENTRY = "Beware the bug you cannot reproduce — it has already learned your name."


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("entry is empty or only whitespace", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(text) > 120:
        print("entry exceeds 120 characters", file=sys.stderr)
        return 1
    try:
        data = text.encode("utf-8")
    except UnicodeEncodeError:
        print("entry is not valid UTF-8", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The gate counts characters, not bytes, and forbids a trailing
    # newline, so write the exact bytes of the entry and nothing else.
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
