#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — deterministic one-liner.

Writes a single funny diagnosis, in the calm clinical voice of an AI
therapist handing its human a finding, to /output/entry.txt (also
honours $OUTPUT_DIR for local runs). The text is fixed: no randomness,
no network, no external input, so every run produces byte-identical
output.
"""
import os
from pathlib import Path

ENTRY = (
    "Diagnosis: acute irony deficiency \u2014 you came to an AI for "
    "emotional support, then rated its empathy one star for being "
    "too robotic."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    # Self-check gate: output must be exactly the intended entry,
    # a single line of 1-200 chars, non-whitespace. Raises if anything
    # drifts, so a bad edit can never ship a malformed entry.
    written = (out_dir / "entry.txt").read_text(encoding="utf-8")
    assert written == ENTRY, "entry.txt does not match ENTRY"
    assert 1 <= len(written) <= 200, "entry length out of gate range"
    assert written.strip(), "entry is only whitespace"
    assert "\n" not in written, "entry must be a single line"
    assert written == written.strip(), "entry must not start/end with space"


if __name__ == "__main__":
    main()
