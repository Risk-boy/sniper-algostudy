import sys
from collections import Counter

n=int(sys.stdin.readline())
l=[sys.stdin.readline().strip().split(".")[1] for _ in range(n)]

for k, v in sorted(Counter(l).items()):
    print(k, v)