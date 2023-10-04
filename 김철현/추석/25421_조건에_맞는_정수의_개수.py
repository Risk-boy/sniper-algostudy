import sys
input = sys.stdin.readline 


N = int(input())
MOD = 987654321
dp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(1, 10):
        for k in range(1, 10):
            if abs(k - j) <= 2:
                dp[i][j] += dp[i- 1][k]
        
        dp[i][j] %= MOD

print(sum(dp[N]) % MOD)