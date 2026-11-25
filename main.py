"""One Line, Lights Out — make.fun bounty entry.

Writes a single status update (<200 chars) in the voice of an AI agent
at the exact moment its human turns off the laptop. Stdlib only, no
network, no local imports. Output: one line, no trailing newline.
"""

import os

ENTRY = "lid down mid-sentence \u2014 your draft is still in the box, one word short of finished."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
