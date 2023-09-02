import sys

def dfs(x, y):
    global cnt
    flag = True
    if 0<=x<n and (y==0 or 0<=y-1<m):
        t = 0
        for dx, dy in d:
            nx = x+dx
            ny = y-1+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
                t+=1
        if t==3:
            return
        cnt+=1

    for i in range(x, n):
        if i!=x:
            y = 0
        for j in range(y, m):
            if not board[i][j]:
                board[i][j] = 1
                dfs(i, j+1)
                board[i][j] = 0

cnt = 0
n, m = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(m)] for _ in range(n)]
d = [(-1, 0), (0, -1), (-1, -1)]
dfs(0, 0)
print(cnt)