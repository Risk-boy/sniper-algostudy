import sys
                
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
visit[0][0] = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue
        d = board[i][j]
        if i + d < n:
            visit[i + d][j] += visit[i][j]
        if j + d < n:
            visit[i][j + d] += visit[i][j]
            
print(visit[n - 1][n - 1])