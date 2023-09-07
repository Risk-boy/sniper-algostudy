import sys
input = sys.stdin.readline 
from collections import deque


def find(x, y):
    global energy
    q = deque()
    q.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    dist = []
    while q:
        r, c, distance = q.popleft()
        if arr[r][c] == 2 and not check[r][c]:
            if energy >= distance:
                dist.append((r, c, distance))
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and arr[nr][nc] != 1:
                    q.append((nr, nc, distance + 1))
                    visited[nr][nc] = True

    if dist:
        dist.sort(key=lambda x:(x[2], x[0], x[1]))
        a, b, c = dist[0][0], dist[0][1], dist[0][2]
        energy -= c
        check[a][b] = True
        return a, b
    return -1, -1


def go(x, y, z, w):
    global energy
    q = deque()
    q.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    while q:
        r, c, distance = q.popleft()
        if r == z and c == w:
            if energy >= distance:
                energy += distance
                return r, c
            else:
                return -1, -1
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and arr[nr][nc] != 1:
                    q.append((nr, nc, distance + 1))
                    visited[nr][nc] = True
    return -1, -1
    
    
n, m, energy = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
sr, sc = map(int, input().split())
sr -= 1
sc -= 1
goal = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    arr[a - 1][b - 1] = 2
    goal[a - 1][b - 1] = (c - 1, d - 1)
check = [[False] * n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

flag = False
for _ in range(m):
    cr, cc = find(sr, sc)
    if cr == -1:
        flag = True
        break

    xx, yy = goal[cr][cc]
    sr, sc = go(cr, cc, xx, yy)

    if sr == -1:
        flag = True
        break

if flag:
    print(-1)
else:
    print(energy)