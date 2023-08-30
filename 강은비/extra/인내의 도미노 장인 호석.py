import sys

def dfs(x, y, d):
    global cnt
    if x<0 or x>=n or y<0 or y>=m :
        return
    
    k = board[x][y] -1
    dx, dy = dr[d]
    for _ in range(k):
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<m and visit[nx][ny] == "S":
            visit[nx][ny] = "F"
            cnt+=1
            dfs(nx, ny, d)
        x, y = nx, ny
    
n, m, r = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [["S" for _ in range(m)] for _ in range(n)]
dr = {"E":(0, 1), "W":(0, -1), "S":(1, 0), "N":(-1, 0)}

cnt = 0
for i in range(r*2):
    if i%2 == 0:
        x, y, d = sys.stdin.readline().split()
        x, y = int(x), int(y)
        if visit[x-1][y-1] == "S":
            visit[x-1][y-1] = "F"
            cnt+=1
            dfs(x-1, y-1, d)
                
    else:
        x, y = map(int, sys.stdin.readline().split())
        visit[x-1][y-1] = "S"
        
print(cnt)
for x in visit:
    print(*x)