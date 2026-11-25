"""Write the GPS's excuse to the output file.

The entry is one line of plain text, at most 200 characters, in the
GPS's own voice: defensive, blaming the map, no dialogue tags.
"""

import os
from pathlib import Path

LINE = "In my defence, the map said turn left. The lake didn't object, and the wedding guests were surprisingly understanding about the car."
# 132 characters: the GPS blames the map, then the lake and the wedding
# guests it drove into. The turn is the car ending up in the lake.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
