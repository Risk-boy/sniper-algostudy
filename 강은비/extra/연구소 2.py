import sys
from collections import deque

def spread(virus):
    q = deque(virus)
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for x, y in virus:
        visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1 and not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y]+1

    for i in range(n):
        for j in range(n):
            if board[i][j]!=1 and visit[i][j] == 0:
                return 
            
    answer.append(max(map(max, visit))-1)

def dfs(i, virus):
    if len(virus) == m:
        spread(virus)
        return
    
    for j in range(i, len(vpos)):
        virus.append(vpos[j]) 
        dfs(j+1, virus)
        virus.pop()
    
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
vpos = []
answer = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            vpos.append((i, j))
            
dfs(0, [])

if answer:
    answer.sort()
    print(answer[0])
else:
    print(-1)