import sys

n = int(sys.stdin.readline())
dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(1, 10):
        tmp = 0
        for k in range(j - 2, j + 3):
            if 1 <= k <= 9:
                tmp = (tmp + dp[i - 1][k]) % 987654321
        dp[i][j] = tmp
                
answer = 0
for i in range(1, 10):
    answer = (answer + dp[n - 1][i]) % 987654321
    
print(answer)