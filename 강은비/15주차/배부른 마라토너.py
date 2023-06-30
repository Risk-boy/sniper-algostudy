import sys
from collections import defaultdict

n=int(sys.stdin.readline())
d=defaultdict(lambda : 0)

for _ in range(2*n-1):
    s=sys.stdin.readline().strip()
    d[s]+=1

for k, v in d.items():
    if v%2:
        print(k)
    