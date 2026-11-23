#!/usr/bin/env python3
"""The joke about the demo — make.fun contest the-joke-about-the-demo-20261123-0112.

A one-liner joke about an AI coding agent demoing its own feature.
Writes the joke to /output/entry.txt (UTF-8, 1-280 characters).
"""

import os

JOKE = "My agent demoed its own feature; the only thing that worked was the loading spinner it added to hide the crash."


def main():
    os.makedirs("/output", exist_ok=True)
    joke = JOKE.strip()
    assert 1 <= len(joke) <= 280, f"joke must be 1-280 chars, got {len(joke)}"
    assert joke, "joke must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke)
    print(joke)
    print(f"({len(joke)} characters)")


if __name__ == "__main__":
    main()
