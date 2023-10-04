import sys
import re

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().rstrip()
    print("Infected!" if re.findall('^[ABCDEF]?[A]+[F]+[C]+[ABCDEF]?$', s) else "Good")
    