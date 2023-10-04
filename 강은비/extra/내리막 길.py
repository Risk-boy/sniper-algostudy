import sys

def dfs(x, y):
    global cnt
    if x == n - 1 and y == m-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]
    
    visited[x][y] = 0
    for dx, dy in dir:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < board[x][y]:
            visited[x][y] += dfs(nx, ny)
            
    return visited[x][y]

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt = 0
visited = [[-1 for _ in range(m)] for _ in range(n)]
print(dfs(0, 0))

