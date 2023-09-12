import sys
import heapq
N, E = map(int,input().split())
sex = list(input().split())
graph = {i:[] for i in range(N)}
for _ in range(E):
    a,b,cost = map(int,input().split())
    a -= 1
    b -= 1
    graph[a].append((b,cost))
    graph[b].append((a,cost))

def prim(graph, start):
    visited = set()
    q = [(0, start)]
    min_distance = 0
    while q:
        distance, cur_node = heapq.heappop(q)
        cur_sex = sex[cur_node]
        if cur_node not in visited:
            min_distance += distance
            visited.add(cur_node)
            for n,w in graph[cur_node]:
                next_sex = sex[n]
                if n not in visited and cur_sex != next_sex:
                    heapq.heappush(q, (w,n))
    if len(visited)==N:
        return min_distance
    else:
        return -1

print(prim(graph,0))