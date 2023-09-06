import sys
from heapq import heappush, heappop

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    parent[y] = x
    return True

n, m = map(int, sys.stdin.readline().split())
pos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
edges = []
parent = [i for i in range(n)]
answer = 0.0
cnt = 0

for i in range(n):
    for j in range(i+1, n):
        heappush(edges, (((pos[i][0]-pos[j][0])**2 + (pos[i][1]-pos[j][1])**2)**0.5, i, j))

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if union(u-1, v-1):
        cnt+=1
    
while edges:
    d, u, v = heappop(edges)
    if union(u, v):
        answer += d
        cnt+=1
        
    if cnt == n-1:
        break
        
print(f"{answer:.2f}")
    

