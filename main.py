"""The Moon Finally Answers Back — make.fun entry.

Writes a single line (1-240 characters) to /output/entry.txt: the Moon
finally replying to everyone who has ever stared up at it, wished on it,
howled at it, and made it late-night promises.

Python standard library only. Fully deterministic: the same line is
written on every run.
"""

import os

LINE = (
    "You wished on me, howled at me, and promised me you'd change at 2 a.m. "
    "Four billion years of night shifts \u2014 and not one of you has ever "
    "wished me goodnight back."
)


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"entry is {len(LINE)} characters, must be 1-240")
    if LINE != LINE.strip() or "\n" in LINE:
        raise ValueError("entry must be a single line with no surrounding space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
