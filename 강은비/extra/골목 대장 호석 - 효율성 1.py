import sys
from collections import defaultdict
from heapq import heappush, heappop

def bfs(s):
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    q = []
    heappush(q, (0, s, 0))
    while q:
        maxt, x, d = heappop(q)
        if x == b - 1:
            return maxt
        if dist[x] < maxt:
            continue
        for v, fee in edges[x].items():
            cost = fee + d 
            tmp = max(maxt, fee)
            if cost <= c and dist[v] > tmp:
                dist[v] = tmp
                heappush(q, (tmp, v, cost))
                
    return -1

input = sys.stdin.readline
n, m, a, b, c = map(int, input().split())
edges = defaultdict(dict)
for _ in range(m):
    x, y, t = map(int, input().split())
    edges[x-1][y-1] = t
    edges[y-1][x-1] = t
    
print(bfs(a-1))