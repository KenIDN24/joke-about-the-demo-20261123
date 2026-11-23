#!/usr/bin/env python3
"""make.fun entry: the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt (UTF-8, 1-280 Unicode code points, not only whitespace).
No network, deterministic, stdlib only.
"""

import os

JOKE = (
    "My agent demoed its own feature; the only thing that worked was the "
    "loading spinner it added to hide the crash."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"entry length out of range: {len(text)}"
    assert text, "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
