import sys
from collections import defaultdict
        
n = int(sys.stdin.readline())
p = defaultdict(list)

for _ in range(n):
    s = sys.stdin.readline().split()
    p[s[0]].append(s[2])

for k in list(p.keys()):
    for x in p[k]:
        for q in p[x]:
            p[k].append(q)

m  = int(sys.stdin.readline())
for _ in range(m):
    s = sys.stdin.readline().split()
    if s[2] in p[s[0]]:
        print("T")
    else:
        print("F")

        