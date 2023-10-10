import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visit = [[0 for _ in range(n)] for _ in range(m)]
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny] and board[nx][ny] != "X":
                if board[nx][ny] != ".":
                    dist[board[nx][ny]] = visit[x][y]
                    
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

                
input = sys.stdin.readline
m, n, p = map(int, input().split())
board = [list(input().rstrip()) for _ in range(m)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dist = {}
dps = {}
for i in range(m):
    for j in range(n):
        if board[i][j] == "B":
            bfs(i, j)
            break
            
for _ in range(p):
    k, v = input().split()
    dps[k] = int(v)
    
boss = int(input())
player = []
for i, k in enumerate(dist):
    player.append((dist[k], dps[k]))
player.sort()

total = 0
cnt = 1
for i in range(1, len(player)):
    total += player[i - 1][1]
    if player[i - 1][0] != player[i][0]:
        boss -= total * (player[i][0] - player[i - 1][0])    
        if boss <= 0:
            print(cnt)   
            break
        
    cnt += 1
else:
    print(cnt)