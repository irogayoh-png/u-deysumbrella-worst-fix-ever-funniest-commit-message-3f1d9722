#!/usr/bin/env python3
"""Worst Fix Ever entry: one commit message for a fix that made it worse.

The line: a tired engineer "fixes" a slow site by caching the homepage
for everyone, so every visitor now sees the same account. On-topic
(criterion 1), the punch is a surreal image rather than a complaint
(criterion 2), the irony is specific to caching -- one shared page means
one shared identity (criterion 3), it reads like a plain commit subject
(criterion 4), and the angle is fresh: identity collapse from a cache,
not reverting, not testing in production, not breaking everything
(criterion 5).

Writes exactly these bytes to entry.txt (no trailing newline),
deterministically, so two runs agree byte for byte. Stdlib only.
MAKEFUN_OUTPUT_DIR stands in for /output outside the grader's container.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = "fix: cached the homepage for everyone; every user is now the same person"


def main():
    # Gate check, same rule as the sealed scorer: 1-100 chars, not blank.
    assert 1 <= len(ENTRY) <= 100 and ENTRY.strip(), "entry out of gate"
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()
