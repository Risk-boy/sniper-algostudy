import sys

def check(sx, sy, n):
    num = board[sx][sy]
    for i in range(sx, sx+n):
        for j in range(sy, sy+n):
            if board[i][j] != num:
                return False
    return True

def bfs(sx, sy, n):
    if check(sx, sy, n):
        if board[sx][sy] == -1:
            answer[0] += 1
        elif board[sx][sy] == 0:
            answer[1] += 1
        else:
            answer[2] += 1
    else:
        for i in range(3):
            for j in range(3):
                bfs(sx+i*n//3, sy+j*n//3, n//3)
        
    
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = [0, 0, 0]
bfs(0, 0, n)

for x in answer:
    print(x)