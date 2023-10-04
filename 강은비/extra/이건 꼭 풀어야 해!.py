import sys

input = sys.stdin.readline

n, q = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

dp = [0 for _ in range(n + 1)]
for i in range(n):
    dp[i + 1] += dp[i] + num[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(dp[r] - dp[l - 1])