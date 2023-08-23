import sys
from collections import defaultdict, deque

def bfs(x):
    q = deque([(-1, x)])
    while q:
        p, x = q.popleft()
        for u in edges[x]:
            if visit[u] and p!=u:
                return False
            if not visit[u]:
                q.append((x, u))
                visit[u] = 1
    return True

k = 1                
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n==0 and m==0:
        break
    
    edges = defaultdict(list)
    visit = [0 for _ in range(n)]
    cnt = 0
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)
    
    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            if bfs(i):
                cnt+=1
                
    if cnt == 0:
        print(f"Case {k}: No trees.")   
    elif cnt == 1:
        print(f"Case {k}: There is one tree.") 
    else:
        print(f"Case {k}: A forest of {cnt} trees.")   

    k+=1