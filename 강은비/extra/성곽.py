import sys
from collections import deque

def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            dx, dy = dir[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                if board[x][y] & (2 ** i):
                    continue
                visit[nx][ny] = k + 1
                q.append((nx, ny))
                cnt += 1
                
    return cnt            

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
visit = [[0 for _ in range(n)] for _ in range(m)]
room = []
k = 0
for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            visit[i][j] = k + 1
            room.append(bfs(i, j))
            k += 1

newvisit = [[0 for _ in range(n)] for _ in range(m)]
mcnt = max(room)
for i in range(m):
    for j in range(n):
        if not newvisit[i][j]:
            newvisit[i][j] = 1
            roomidx = visit[i][j]
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for d in range(4):
                    dx, dy = dir[d]
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not newvisit[nx][ny]:
                        if board[x][y] & (2 ** d):
                            if visit[nx][ny] != roomidx:
                                mcnt = max(mcnt, room[roomidx - 1] + room[visit[nx][ny] - 1])
                            continue
                        
                        newvisit[nx][ny] = 1
                        q.append((nx, ny))
print(k)
print(max(room))
print(mcnt)
                        