import sys 
import heapq
input = sys.stdin.readline
N,M = map(int,input().split())

def prim(graph, start):
    visited = set()
    mst_cost = 0
    priority_queue = [(0, start)]

    while priority_queue:
        cost, cur = heapq.heappop(priority_queue)
        if cur not in visited:
            visited.add(cur)
            mst_cost += cost
            for neighbor, weight in graph[cur]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight,neighbor))
    return mst_cost

graph = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

print(prim(graph,list(graph.keys())[0]))

