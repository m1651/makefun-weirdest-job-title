#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown - make.fun bounty entry.

Writes a single original job title (1-60 characters) to /output/entry.txt.
Python 3, stdlib only, no network, fully deterministic.
"""

import os
import sys

MAX_CHARS = 60

LINE = "Senior Taste-Tester of Gas Station Sushi"


def main() -> None:
    # Validate the line before writing: the gate requires UTF-8 text
    # of 1 to 60 characters, not only white space, on a single line.
    if not LINE.strip():
        print("error: entry line is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(LINE) > MAX_CHARS:
        print(
            "error: entry line is %d characters, over the %d limit"
            % (len(LINE), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in LINE or "\r" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        sys.exit(1)
    # A judged one-liner must not spend characters on invisible padding:
    # leading or trailing whitespace would count toward the limit.
    if LINE != LINE.strip():
        print(
            "error: entry line must not start or end with whitespace",
            file=sys.stderr,
        )
        sys.exit(1)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %d characters to %s" % (len(LINE), out_path))


if __name__ == "__main__":
    main()
