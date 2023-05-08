import sys, heapq
# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = int(1e9)


n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))

dijkstra(x)
flag = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)