import sys
input = sys.stdin.readline 


while True:
    n = int(input())
    if n == 0:
        break
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        p = int(input())
        dp[i] = max(p, dp[i - 1] + p)
    print(max(dp[1:]))