import sys

[n, m] = list(map(int, sys.stdin.readline().rstrip().split()))
edges = {tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)}

def BF(n, edges):
    dist = [float("Inf")] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        for (u, v, w) in edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for (u, v, w) in edges:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print(-1)
            return
        
    for d in dist[2:]:
        if d == float("Inf"):
            print(-1)
        else:
            print(d)
    return

BF(n, edges)