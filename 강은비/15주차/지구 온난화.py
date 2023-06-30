import sys

r, c=map(int, sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(r)]
newboard=[[0 for _ in range(c)] for _ in range(r)]
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
posx=[]
posy=[]

for x in range(r):
    for y in range(c):
        cnt=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (nx<0 or nx>=r or ny<0 or ny>=c) or (0<=nx<r and 0<=ny<c and board[nx][ny]=="."):
                cnt+=1
        if cnt>=3:
            newboard[x][y]="."
        else:
            newboard[x][y]=board[x][y]
            if board[x][y]=="X":
                posx.append(x)
                posy.append(y)
posx.sort()
posy.sort()
for i in range(posx[0], posx[-1]+1):
    for j in range(posy[0], posy[-1]+1):
        print(newboard[i][j], end="")
    print()