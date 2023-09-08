import sys
from collections import defaultdict, deque

def bfs(s):
    q = deque([s])
    while q:
        x = q.popleft()
        for v in edges[x]:
            if not parent[v]:
                parent[v] = x+1
                q.append(v)

edges = defaultdict(list)
n = int(sys.stdin.readline())
parent = [0 for _ in range(n)]
parent[0] = -1
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
    
bfs(0)
for i in range(1, n):
    print(parent[i])