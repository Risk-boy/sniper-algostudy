import sys
from collections import deque

def fire():
    global fpos
    tmp = []
    for x, y in fpos:
        for k in range(4):
            nx = x+d[k][0]
            ny = y+d[k][1]
            if 0<=nx<r and 0<=ny<c and board[nx][ny]!="#" and board[nx][ny]!="F":
                board[nx][ny] = "F"
                tmp.append((nx, ny))
    fpos = tmp
    
def bfs(jx, jy):
    q = deque([(jx, jy)])
    while q:
        for _ in range(len(q)):
            x, y= q.popleft()
            if x==0 or x==r-1 or y==0 or y==c-1:
                return visit[x][y]
            for i in range(4):
                nx = x+d[i][0]
                ny = y+d[i][1]
                if 0<=nx<r and 0<=ny<c and board[nx][ny] == "." and not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y]+1
                    q.append((nx, ny))
        fire()        
        
r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
visit = [[0 for _ in range(c)] for _ in range(r)]
fpos = deque()
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
jx=jy=-1

for i in range(r):
    for j in range(c):
        if board[i][j] == "J":
            jx, jy = i, j
            visit[jx][jy] = 1
        if board[i][j] == "F":
            fpos.append((i, j))
fire()            
answer = bfs(jx, jy)       
             
if answer:
    print(answer)
else:   
    print("IMPOSSIBLE")
