import sys
import copy
sys.setrecursionlimit(10**5)
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
directions = [(0,1),(0,-1),(1,0),(-1,0)]


def dfs(x, y, visited, new_graph):
    visited[x][y] = True

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and new_graph[nx][ny] > 0:
            dfs(nx, ny, visited, new_graph)


max_height = max(max(row) for row in graph)
answer = -1

for rain in range(max_height + 1):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    new_graph = [[graph[i][j] - rain for j in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):
            if new_graph[i][j] > 0 and not visited[i][j]:
                dfs(i, j, visited, new_graph)
                cnt += 1

    answer = max(answer, cnt)

print(answer)


    
    
