import sys

def star(x, y, k):
    if k == 1:
        board[x][y] = "*"
        board[x+1][y-1] = "*"
        board[x+1][y+1] = "*"
        board[x+2][y-2] = "*"
        board[x+2][y-1] = "*"
        board[x+2][y] = "*"
        board[x+2][y+1] = "*"
        board[x+2][y+2] = "*"
        return 
    
    k = k>>1
    star(x, y, k)
    star(x+k*3, y-k*3, k)
    star(x+k*3, y+k*3, k)
    
        
n = int(sys.stdin.readline())
board = [[" " for _ in range(2*n-1)] for _ in range(n)]
star(0, n-1, n//3)
for x in board:
    print("".join(x))
