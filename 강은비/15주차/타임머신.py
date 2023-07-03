import sys
from collections import defaultdict

def bf(s):
    distance[s]=0
    for i in range(n):  
        for x in range(n):  #모든 정점의 모든 엣지
            for y, v in edges[x]:
                if distance[x]!=float("inf") and distance[y]>distance[x]+v:
                    distance[y]=distance[x]+v
                    if i==n-1:
                        return True
    return False


edges=defaultdict(list)
n, m=map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b, c=map(int, sys.stdin.readline().split())
    edges[a-1].append((b-1, c))

distance=[float("inf")]*n
res=bf(0)
#print(distance)
if res:
    print(-1)
else:
    for i in range(1, n):
        if distance[i]==float("inf"):
            print(-1)
        else:
            print(distance[i])
