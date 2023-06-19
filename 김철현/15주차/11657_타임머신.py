import sys
input = sys.stdin.readline


INF = int(1e9)
def solve(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur = graph[j][0]
            next = graph[j][1]
            cost = graph[j][2]

            if dist[cur] != INF and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n-1:
                    return True

    return False

n, m = map(int, input().split())
graph = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

negative_cycle = solve(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])