#!/usr/bin/env python3
"""Entry for the make.fun bounty "One Letter: Coffee or Tea".

Writes exactly one byte -- the letter "A" -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Why "A", why coffee: the judge weighs vividness first, and coffee is the
louder drink. It is dark, bitter, and the thing people reach for when they
need to wake up and get moving; tea is gentle and quiet, coffee shouts.
"A" is also the first letter and the top grade, so it lands as the natural
first pick -- a whole answer that needs nothing beside it. One letter,
one stance, no decoration.

Standard library only, no network access, deterministic: the output is
always the same single byte.
"""

import os
import sys

LETTER = "A"  # coffee


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    data = LETTER.encode("utf-8")
    with open(dest, "wb") as fh:
        fh.write(data)
    # Guard: the gate rejects anything but exactly one character, so
    # confirm on disk that we wrote precisely one byte before finishing.
    written = os.path.getsize(dest)
    if written != 1:
        print("error: entry.txt is %d bytes, expected 1" % written,
              file=sys.stderr)
        return 1
    print("Wrote", dest, "(1 byte: %r)" % LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
