import sys
from collections import deque
n, m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dir={1:(0, -1), 2:(-1, -1), 3:(-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}
clouds=deque([[n-1, 0], [n-1, 1], [n-2, 0], [n-2,1]]); cpos=[[0 for _ in range(n)] for _ in range(n)]

def makerain(d, s):
    global board
    global clouds
    for p in clouds:
        p[0]=(p[0]+dir[d][0]*s+n)%n
        p[1]=(p[1]+dir[d][1]*s+n)%n
    for x, y in clouds:
        board[x][y]+=1
        cpos[x][y]=1    

def waterbug():
    global board
    global clouds
    while clouds:
        x, y=clouds.popleft()
        for d in (2,4,6,8):
            nx=x+dir[d][0]; ny=y+dir[d][1]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]:
                board[x][y]+=1

    for i in range(n):
        for j in range(n):
            if board[i][j]>=2:
                if not cpos[i][j]:
                    clouds.append([i, j])
                    board[i][j]-=2
            if cpos[i][j]:
                cpos[i][j]=0

for _ in range(m):
    d, s=map(int, sys.stdin.readline().split())
    makerain(d, s)
    waterbug()
print(sum(map(sum, board)))