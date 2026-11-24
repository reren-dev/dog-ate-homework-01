#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, in the dog's own voice, to /output/entry.txt.
The dog believes it has done nothing wrong.
"""

import os

EXCUSE = (
    "I ate it because it smelled like 2 a.m. and suffering, "
    "so I finished it for you. I also buried the bibliography. "
    "You're welcome."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
