import sys
input = sys.stdin.readline 


n = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        t = arr[j][0]
        p = arr[j][1]
        if j + t - 1 <= i:
            dp[i] = max(dp[i], dp[j - 1] + p)

print(max(dp[1:n + 1]))