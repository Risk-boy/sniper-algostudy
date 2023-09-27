import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for a in range(n):
        for b in range(n):
            if dist[a][b] > dist[a][k] + dist[k][b]:
                dist[a][b] = dist[a][k] + dist[k][b]

for _ in range(m):
    a, b, c = map(int, input().split())
    print("Enjoy other party" if dist[a - 1][b - 1] <= c else "Stay here")