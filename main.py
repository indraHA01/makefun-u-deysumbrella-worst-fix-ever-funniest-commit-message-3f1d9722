"""Worst Fix Ever: Funniest Commit Message.

make.fun competition u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.

The entry is a single commit message for a bug fix that made everything
worse. The program writes that one line to /output/entry.txt (or to
$ENTRY_OUTPUT_DIR/entry.txt when the variable is set, for local testing).

The line: the fix "worked" — bug reports dropped 100% — because the fix
deleted the button users clicked to report bugs. The metric improved by
removing the thing that measured it.
"""

import os
import sys

# The entry: one line, at most 100 characters, plain commit-subject voice.
ENTRY = "fix: removed the report button, bug reports down 100%"

MAX_CHARS = 100


def main() -> int:
    """Validate the entry against the gate, then write it out."""
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"error: entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
