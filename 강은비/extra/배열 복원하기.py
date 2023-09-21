import sys

input = sys.stdin.readline
h, w, x, y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h + x)]
a = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        a[i][j] = board[i][j]
for i in range(x, h):
    for j in range(y, w):
        a[i][j] -= a[i - x][j - y]
        
for x in a:
    print(*x)