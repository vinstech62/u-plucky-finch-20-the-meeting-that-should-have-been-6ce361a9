"""Entry for make.fun bounty u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.

Writes exactly one line — a joke about a meeting that should have
been an email — to /output/entry.txt (or $ENTRY_OUTPUT).
"""

import os
from pathlib import Path

ENTRY = "After an hour, we finally agreed on the follow-up email. It just said: 'Per my last meeting.'"


def main() -> None:
    # Self-checks: the harness requires exactly one line, 1-200 UTF-8
    # chars, no trailing newline, and no leading/trailing whitespace
    # that would make the line read as two entries.
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be exactly one line"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(ENTRY.encode("utf-8")) <= 200, "entry must be 1-200 UTF-8 chars"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    out.chmod(0o644)
    # Verify what was actually written, not just what was intended.
    written = out.read_text(encoding="utf-8")
    assert written == ENTRY, "written output differs from ENTRY"


if __name__ == "__main__":
    main()
