import sys
from collections import defaultdict, deque

edges = defaultdict(list)
n, w = map(int, sys.stdin.readline().split())
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)

cnt = 0
for k, v in edges.items():
    if len(v)==1 and k!=1:
        cnt+=1
print(w/cnt)


'''
import sys
from collections import defaultdict, deque

def bfs(s):
    q = deque([s])
    while q:
        u = q.popleft()
        visit[u] = 1
        t = water[u]
        cnt = len(edges[u]) if u == 0 else len(edges[u])-1
        for x in edges[u]:
            if not visit[x]:
                water[x]+=t/cnt
                q.append(x)
                water[u] = 0

edges = defaultdict(list)
n, w = map(int, sys.stdin.readline().split())
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)

water = [0 for _ in range(n)]
visit = [0 for _ in range(n)]
water[0] = w
bfs(0)
print(sum(water)/len([x for x in water if x>0]))
'''