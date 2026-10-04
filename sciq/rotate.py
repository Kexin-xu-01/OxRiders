"""Rotate the vague-reference word across 4 phrasings to blunt a single-token shortcut."""
import re
import sys

SYN = ["particular", "certain", "given", "specific"]

for p in sys.argv[1:]:
    s, n = open(p).read(), [0]

    def sub(m):
        w = SYN[n[0] % 4]
        n[0] += 1
        return w.capitalize() if m.group()[0] == "P" else w

    open(p, "w").write(re.sub(r"\b[Pp]articular\b", sub, s))
