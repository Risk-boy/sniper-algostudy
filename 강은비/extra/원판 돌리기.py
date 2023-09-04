import sys
from collections import deque

def move():
    for i in range(n):
        if (i+1) % x == 0:
            if d == 0:
                board[i].rotate(k)
            else:
                board[i].rotate(-k)

def bfs(x, y):
    global flag
    q = deque([(x, y)])
    k = board[x][y] 
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and -1<=ny<=m and not visit[nx][ny%m] and k == board[nx][ny%m]:
                flag = True
                visit[nx][ny%m] = 1
                q.append((nx, ny%m))
                board[nx][ny%m] = "."

def change():
    s = [x for row in board for x in row if x != "."]
    if s:
        mean = sum(s)/len(s)
        for i in range(n):
            for j in range(m):
                if board[i][j] != ".":
                    if board[i][j] > mean:
                        board[i][j] -= 1
                    elif board[i][j] < mean:
                        board[i][j] += 1
   
n, m, t = map(int, sys.stdin.readline().split())
board = [deque(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
for _ in range(t):
    x, d, k = map(int, sys.stdin.readline().split())
    move()
    visit = [[0 for _ in range(m)] for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(m):
            if board[i][j] != "." and not visit[i][j]:
                bfs(i, j)
    if not flag:
        change()
        
print(sum([x for row in board for x in row if x != "."]))