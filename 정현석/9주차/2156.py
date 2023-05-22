import sys

n = int(sys.stdin.readline().rstrip())

glasses = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [glasses[0] if i ==0 else glasses[0]+glasses[1] if i==1 else 0 for i in range(n)]

for i in range(2, n):
    dp[i] = max(max(dp[i-3] + glasses[i-1] + glasses[i], dp[i-2] + glasses[i]), dp[i-1])

print(dp[n-1])