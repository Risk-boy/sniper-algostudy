import sys
from collections import deque

def move():
    for j in range(6):
        for i in range(11, -1, -1):
            k = i-1
            while board[i][j] == -1:
                if i==0 or k<0:
                    board[i][j] = "."
                    continue
                if board[k][j] != -1:
                    board[i][j], board[k][j] = board[k][j], board[i][j]
                k-=1

def bfs(x, y, ch):
    q = deque([(x, y, 1)]) 
    pos = set()
    pos.add((x, y))
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<12 and 0<=ny<6 and board[nx][ny]==ch and not visit[nx][ny]:
                q.append((nx, ny, cnt+1))
                visit[nx][ny] = 1
                pos.add((nx, ny))
         
    if len(pos)>=4:
        for x, y in pos:
            board[x][y] = -1
        return True
    return False

board = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
while True:
    flag = 0
    visit = [[0 for _ in range(6)] for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != "." and not visit[i][j]:
                visit[i][j] = 1
                if bfs(i, j, board[i][j]):
                    flag = 1
    
    move()
    if flag:
        cnt+=1
    else:
        print(cnt)
        break