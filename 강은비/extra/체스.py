import sys

def position(pos, mark):
    for i in range(0, len(pos), 2):
        board[pos[i] - 1][pos[i + 1] - 1] = mark
        
input = sys.stdin.readline

n, m = map(int, input().split())
qn, *qpos = map(int, input().split())
kn, *kpos = map(int, input().split())
pn, *ppos = map(int, input().split())

board = [[0 for _ in range(m)] for _ in range(n)]
kdir = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
qdir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
  
position(qpos, "q")
position(kpos, "k")
position(ppos, "p")

for i in range(0, len(kpos), 2):
    x, y = kpos[i] - 1, kpos[i + 1] - 1
    for dx, dy in kdir:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            board[nx][ny] = 1
            
for i in range(0, len(qpos), 2):
    x, y = qpos[i] - 1, qpos[i + 1] - 1
    for dx, dy in qdir:
        nx = x + dx
        ny = y + dy
        while 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 0 or board[nx][ny] == 1:
                board[nx][ny] = 1
                nx += dx
                ny += dy
            else:
                break
    
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cnt += 1
            
print(cnt)
