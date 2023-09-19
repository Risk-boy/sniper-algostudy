import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [float("inf") for _ in range(n)]
dp[0] = 0
for i in range(n):
    if a[i]:
        for j in range(i + 1, i + 1 + a[i]):
            if j == n:
                break
            dp[j] = min(dp[i] + 1, dp[j])
            
if dp[n - 1] == float("inf"):
    print(-1)
else:
    print(dp[n - 1])