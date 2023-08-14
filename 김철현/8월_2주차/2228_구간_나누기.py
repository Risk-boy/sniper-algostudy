import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
arr = [0] + [int(input()) for _ in range(n)]

"""
dp[n][m]: n 번째 숫자까지 m개의 구간을 나누었을 때 최대합
1) m번째 구간에 n이 포함 안될 때
    dp[n][m] = max(dp[n][m], dp[n - 1][m])
2) m번째 구간에 n이 포함 될 때
    dp[n][m] = max(dp[n][m], dp[k - 2][m - 1] + sum(k, n))
"""

for i in range(1, n + 1):
    arr[i] += arr[i - 1]

dp = [[-float("inf")] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 0
    
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j]
        for k in range(i, 1, -1):
            dp[i][j] = max(dp[i][j], dp[k - 2][j - 1] + arr[i] - arr[k - 1])
        if j == 1:
            dp[i][j] = max(dp[i][j], arr[i])
print(dp[n][m])