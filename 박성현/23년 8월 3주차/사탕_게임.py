import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
board = [list(input()) for _ in range(n)]

def check(board):
    cnt = 0 
    for i in range(n):
        c_r = 1 
        c_c = 1 
        for j in range(1,n):
            if board[i][j] == board[i][j-1]:
                c_r += 1 
            else:
                c_r = 1
            if board[j][i] == board[j-1][i]:
                c_c += 1
            else:
                c_c = 1
            if c_r > cnt:
                cnt = c_r 
            if c_c > cnt:
                cnt = c_c
    return cnt

result = 0

for i in range(n):
    for j in range(n):
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 가로 방향으로 교환
            temp = check(board)
            if temp > result:
                result = temp
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 다시 원상복구

        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            temp = check(board)
            if temp > result:
                result = temp
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
print(result)