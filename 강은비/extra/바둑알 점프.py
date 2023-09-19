import sys

def dfs(dots):
    if len(dots) == 1:
        print("Possible")
        sys.exit()
        
    for j in range(len(dots)):
        x, y = dots[j]
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 2 and board[nx + dx][ny + dy] == 0:
                board[x][y] = 0
                board[nx][ny] = 0
                board[nx + dx][ny + dy] = 2
                dots.remove((nx, ny)) 
                dots.remove((x, y)) 
                dots.append((nx + dx, ny + dy))     
                dfs(dots)
                board[x][y] = 2
                board[nx][ny] = 2
                board[nx + dx][ny + dy] = 0  
                dots.remove((nx + dx, ny + dy))
                dots.append((nx, ny))
                dots.append((x, y))

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dots = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            dots.append((i, j))
            
dir = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
dfs(dots)
print("Impossible")