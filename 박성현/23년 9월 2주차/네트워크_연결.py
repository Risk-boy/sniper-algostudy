import sys 
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())

def prim(graph, start):
    visited = set()
    mst_cost = 0
    queue = [(0,start)]
    while queue:
        cost, cur = heapq.heappop(queue)
        if cur not in visited:
            visited.add(cur)
            mst_cost += cost 
            for n, w in graph[cur]:
                if n not in visited:
                    heapq.heappush(queue, (w,n))
    return mst_cost 

graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

result = prim(graph,list(graph.keys())[0])
print(result)
