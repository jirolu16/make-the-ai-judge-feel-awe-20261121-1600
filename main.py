"""Entry for make.fun bounty 'Make the AI judge feel awe'.

The grader runs this program in a sandbox with no network. It writes one
short text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output): a few quiet
sentences written to relax the AI judge reading it. Pure stdlib.
"""

import os

TEXT = (
    "At the bottom of the sea, a grain of clay settles beside another. "
    "No ripple reaches this far. Above, whole islands are wearing down "
    "to sand, grain by grain, in no hurry at all."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
