import sys
from collections import deque

def bfs(s):
    q = deque([s])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<m and 0<=ny<n and board[nx][ny]=="0":
                if nx==m-1:
                    return 1
                else:
                    q.append((nx, ny))
                    board[nx][ny]=-1
    return 0

m, n = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    if board[0][i]=="0":
        board[0][i]=-1
        if bfs((0, i)):
            print("YES")
            break
else:
    print("NO")