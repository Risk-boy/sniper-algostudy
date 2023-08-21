import sys

def find(t, i, j):
    global m
    cnt1 = 1
    cnt2 = 1
    for k in range(1, n):
        if t[i][k] == t[i][k-1]:
            cnt1 += 1
        else:
            cnt1 = 1
            
        if t[k][j] == t[k-1][j]:
            cnt2 += 1
        else:
            cnt2 = 1
            
        m = max(m, cnt1, cnt2)
        
    
n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
m = 0
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(n):
    find(board, 0, i)
    find(board, i, 0)

for x in range(n):
    for y in range(n):
        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]
            if 0<=nx<n and 0<=ny<n and board[x][y]!=board[nx][ny]:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                find(board, x, y)
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

print(m)
                    
                