import sys

def move():
    global robot
    new = {}
    for x, y in robot.keys():
        mx = x + (x < jx) - (x > jx)
        my = y + (y < jy) - (y > jy)
        if mx == jx and my == jy:
            return -1
        new[(mx, my)] = new.get((mx, my), 0) + 1
        board[x][y] = "."
        
    robot = {}  
    for x, y in new.keys():
        if new[(x, y)] >= 2:
            continue
        robot[(x, y)] = 1
        board[x][y] = "R" 

input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
jorder = list(map(int, input().rstrip()))
dir = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

robot = {}
for i in range(r):
    for j in range(c):
        if board[i][j] == "I":
            jx, jy = i, j
        if board[i][j] == "R":
            robot[(i, j)] = robot.get((i, j), 0) + 1
            
for i in range(len(jorder)):
    dx, dy = dir[jorder[i] - 1]
    nx = jx + dx
    ny = jy + dy
    if 0 <= nx < r and 0 <= ny < c:
        if board[nx][ny] == "R":
            print("kraj", i + 1)
            break
        else:
            board[jx][jy] = "."
            board[nx][ny] = "I"
            jx, jy = nx, ny
            
    if move() == -1:
        print("kraj", i + 1)
        break
else:    
    for row in board:
        print("".join(row))
    
    
    
