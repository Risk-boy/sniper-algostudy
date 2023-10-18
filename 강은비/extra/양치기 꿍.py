import sys
from collections import deque

def bfs(x, y):
    global wolf, sheep
    
    q = deque([(x, y)])
    w = board[x][y] == "v"
    s = board[x][y] == "k"
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] != "#":
                q.append((nx, ny))
                visited[nx][ny] = 1
                if board[nx][ny] == "k":
                    s += 1
                elif board[nx][ny] == "v":
                    w += 1
                   
    if w >= s:
        wolf += w
        return
    
    sheep += s

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[0 for _ in range(c)] for _ in range(r)]
wolf = sheep = 0
for i in range(r):
    for j in range(c):
        if (board[i][j] == "k" or board[i][j] == "v") and not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j)
            
print(sheep, wolf)
            
