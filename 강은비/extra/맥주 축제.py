import sys
from heapq import heappush, heappop

n, m, k = map(int, sys.stdin.readline().split())
beer = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(k)], key = lambda x: x[1])
q = []
pref = 0

for i in range(k):
    if len(q) < n:
        heappush(q, beer[i][0])
        pref += beer[i][0]
        
    if len(q) == n:
        if pref >= m:
            print(beer[i][1])
            break
        else:
            pref -= heappop(q)
else:
    print(-1)


