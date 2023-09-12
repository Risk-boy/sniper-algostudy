import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()


N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]
graph = {i: [(j, data[i][j]) for j in range(N) if i != j] for i in range(N)}

def prim(graph,start):
    visited = set()
    dist = 0
    q = [(0, start)]
    while q:
        cost, cur_node = heapq.heappop(q)
        if cur_node not in visited:
            visited.add(cur_node)
            dist += cost
            for n, w in graph[cur_node]:
                if n not in visited:
                    heapq.heappush(q, (w,n))
    return dist
result = prim(graph,0)
print(result)





