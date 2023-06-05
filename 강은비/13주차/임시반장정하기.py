import sys
from collections import Counter, defaultdict

n=int(sys.stdin.readline())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

count=defaultdict(set)

for i in range(5):
    cls=defaultdict(set)
    for j in range(n):
        cls[board[j][i]].add(j)
    for k, v in cls.items():
        if len(v)>=2:
            for x in v:
                count[x]|=(v)
if not count:
    print(1)
else:
    print(sorted(count.items(), key=lambda x: (-len(x[1]), x[0]))[0][0]+1)