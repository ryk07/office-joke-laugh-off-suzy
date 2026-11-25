"""One-line office joke entry.

Writes a single original one-line joke about office life to
/output/entry.txt (UTF-8, 1-200 characters, one line).
"""

import os

JOKE = (
    "HR renamed getting fired to 'graduating' \u2014 my diploma came in a "
    "cardboard box, and the farewell cake was one I bought myself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
