import sys
input = sys.stdin.readline


def solve(r, c):
    if r == m -1 and c == n - 1:
        dp[r][c] = 1
        return
    if dp[r][c] != -1: # 방문한적이 있으면
        return
    # 방문한 적이 없으면
    dp[r][c] = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < m and 0 <= nc < n:
            if arr[r][c] > arr[nr][nc]: # 더 높으면
                solve(nr, nc)
                dp[r][c] += dp[nr][nc]

m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
dp = [[-1 for _ in range(n)] for _ in range(m)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
solve(0, 0)
print(dp[0][0])
