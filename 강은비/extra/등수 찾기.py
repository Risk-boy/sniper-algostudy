import sys
from collections import defaultdict, deque

def bfs(edges):
    cnt = 0
    q = deque([x])
    visit = [0 for _ in range(n + 1)]
    visit[x] = 1
    
    while q:
        u = q.popleft()
        for v in edges[u]:
            if not visit[v]:
                q.append(v)
                visit[v] = 1
                cnt += 1
    return cnt

input = sys.stdin.readline
n, m, x = map(int, input().split())
edges1 = defaultdict(list)
edges2 = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    edges1[a].append(b)
    edges2[b].append(a)

print(bfs(edges2) + 1, n - bfs(edges1))

