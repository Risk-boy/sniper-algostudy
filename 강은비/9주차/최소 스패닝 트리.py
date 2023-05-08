import sys
from collections import defaultdict
import heapq

edges=defaultdict(list)
v, e=map(int, sys.stdin.readline().split())
for _ in range(e):
    x, y, w=map(int, sys.stdin.readline().split())
    edges[x].append((w, y))
    edges[y].append((w, x))

visit=[0 for _ in range(v+1)]
visit[1]=1

pq=edges[1]
heapq.heapify(pq)
    
answer=0
while pq:
    w, y=heapq.heappop(pq)  #w가 가장 작은 간선
    if not visit[y]:  #또 방문하는 경우 사이클. -> 트리 유지 
        answer+=w
        visit[y]=1
        for x in edges[y]:
            heapq.heappush(pq, x)
            
print(answer)
        
    