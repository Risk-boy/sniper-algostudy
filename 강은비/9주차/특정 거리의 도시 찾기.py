import sys
from collections import defaultdict, deque

def bfs(s):
    q=deque([s])
    while q:
        x=q.popleft()
        for y in edge[x]:
            if not visit[y] and y!=s:
                q.append(y)
                visit[y]=visit[x]+1

edge=defaultdict(list)
n, m , k, x=map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b=map(int, sys.stdin.readline().split())
    edge[a-1].append(b-1)
    
visit=[0 for _ in range(n)]
bfs(x-1)

flag=False
for i in range(n):
    if visit[i]==k:
        flag=True
        print(i+1)
if not flag:
    print(-1)
        
    