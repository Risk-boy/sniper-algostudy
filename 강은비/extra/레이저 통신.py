import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y, 0, 0, 0)])
    visit[x][y] = [0, {(0, 0)}]
    while q:
        x, y, dx, dy, dist = q.popleft()
        if dist > visit[x][y][0]:
            continue
        if dx == 0 and dy == 0:
            dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        else:
            dir = [(dx, dy), (dy, dx), (-dy, -dx)]
        k = len(dir)
        for i in range(k):
            ndx, ndy = dir[i]
            nx, ny = x + ndx, y + ndy
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
                if k == 4:
                    visit[nx][ny][0] = dist
                    visit[nx][ny][1].add((ndx, ndy))
                    q.append((nx, ny, ndx, ndy, dist))
                else:
                    newd = dist
                    if i > 0:
                        newd = dist + 1
                    if visit[nx][ny][0] >= newd:
                        if visit[nx][ny][1] & {(ndx, ndy)} and visit[nx][ny][0] == newd:
                            continue
                        visit[nx][ny][0] = newd
                        q.append((nx, ny, ndx, ndy, newd))
                        visit[nx][ny][1].add((ndx, ndy))

    
input = sys.stdin.readline
w, h = map(int, input().split())
board = [list(input().rstrip()) for _ in range(h)]
visit = [[[float("inf"), set()] for _ in range(w)] for _ in range(h)]

pos = []
answer = float("inf")
for i in range(h):
    for j in range(w):
        if board[i][j] == "C":
            pos.append((i, j))
bfs(*pos[0])
x, y = pos[1]

print(visit[x][y][0])
