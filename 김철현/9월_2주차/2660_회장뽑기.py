import sys
input = sys.stdin.readline 


n = int(input())
INF = float("inf")
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


min_v = INF
arr = []
for i in range(n):
    temp = max(graph[i])
    if temp < min_v:
        arr = []
        arr.append(i + 1)
        min_v = temp
    elif temp == min_v:
        arr.append(i + 1)

print(min_v, len(arr))

print(*arr)