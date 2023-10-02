import sys
from collections import defaultdict
from heapq import heappop, heappush

def dij(lim):
    q = []
    visit = [float("inf") for _ in range(n)]
    heappush(q, (0, 0))
    while q:
        d, v = heappop(q)
        if d > visit[v]:
            continue
        for x, new in edges[v].items():
            if new > lim:
                if d + 1 < visit[x]:
                    visit[x] = d + 1
                    heappush(q, (d + 1, x))
            else:
                if d < visit[x]:
                    visit[x] = d
                    heappush(q, (d, x))

    return visit[n - 1] <= k

input = sys.stdin.readline
edges = defaultdict(dict)
n, p, k = map(int, input().split())
l = r = 0
answer = -1
for _ in range(p):
    a, b, d = map(int, input().split())
    edges[a - 1][b - 1] = d
    edges[b - 1][a - 1] = d
    r = max(d, r)

while l <= r:
    mid = (l + r) // 2
    if dij(mid):
        r = mid - 1
        answer = mid
    else:
        l = mid + 1
        
print(answer)       

    
