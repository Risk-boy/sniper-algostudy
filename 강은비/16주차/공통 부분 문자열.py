import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

dp=[[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
m = 0
for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] > m:
                m = dp[i][j]
print(m)