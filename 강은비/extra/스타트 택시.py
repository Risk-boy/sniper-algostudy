import sys
from collections import deque
from heapq import heappush, heappop

def bfs(x, y, rx=None, ry=None, find=False):
    global gas
    
    maxd = n**2 + 1
    q = deque([(x, y)])
    result = []
    visit = [[0 for _ in range(n)] for _ in range(n)]
    visit[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        if find and visit[x][y] > maxd:
            gas -= maxd
            return heappop(result)
        
        if visit[x][y] > gas:
            return False
        
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and board[nx][ny] == 0:
                if find and cpos.get((nx,ny), 0):
                    if visit[x][y] <= maxd:
                        maxd = visit[x][y] 
                        heappush(result, (nx, ny))

                if not find and nx == rx and ny == ry:
                    gas += visit[x][y] 
                    return True

                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
                
    return False
                             
n, m, gas = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bx, by = map(int, sys.stdin.readline().split())
bx -= 1
by -= 1
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]

cpos = {}
for _ in range(m):
    sx, sy, dx, dy = map(int, sys.stdin.readline().split())
    cpos[(sx-1, sy-1)] = (dx-1, dy-1)

while cpos:
    if not cpos.get((bx, by), 0):
        result = bfs(bx, by, find = True)    
        if result:
            sx, sy = result
        else:
            print(-1)
            break
    else:
        sx, sy = bx, by
        
    dx, dy = cpos.pop((sx, sy))
    if sx != dx or sy != dy:
        if not bfs(sx, sy, dx, dy):
            print(-1)
            break
    bx, by = dx, dy
else:
    print(gas)
