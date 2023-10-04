import sys
input = sys.stdin.readline 
from heapq import heappush, heappop


def dijkstra(x):
    distance = [INF] * (N + 1)
    distance[1] = 0
    q = []
    heappush(q, (0, 1))
    while q:
        dist, cur = heappop(q)
        
        if distance[cur] < dist:
            continue
        
        for nxt, pay in graph[cur]:
            temp = dist
            if pay > x:
                temp += 1
            
            if distance[nxt] > temp:
                distance[nxt] = temp
                heappush(q, (temp, nxt))

    if distance[N] <= K:
        return True
    else:
        return False

N, P, K = map(int, input().split())
INF = float("inf")
graph = [[] for _ in range(N + 1)]
cost = set()
cost.add(0)
for _ in range(P):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    cost.add(c)
    
cost = sorted(list(cost))
left, right = 0, len(cost) - 1
ans = -1
while left <= right:
    middle = (left + right) // 2
    
    check = dijkstra(cost[middle])
    
    if check:
        right = middle - 1
        ans = cost[middle]
    else:
        left = middle + 1

print(ans)