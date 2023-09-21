import sys

def dfs(i, dist, cnt):
    global answer
    if cnt == n:
        answer = min(answer, dist)
        return 
    
    for j in range(n):
        if not visit[j]:
            visit[j] = 1
            dfs(j, dist + edges[i][j], cnt + 1)
            visit[j] = 0

input = sys.stdin.readline
n, k = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        for v in range(n):
            if edges[i][j] > edges[i][v] + edges[v][j]:
                edges[i][j] = edges[i][v] + edges[v][j]

answer = float("inf")
visit = [0 for _ in range(n)]
visit[k] = 1
dfs(k, 0, 1)
print(answer)