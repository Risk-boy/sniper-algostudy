import sys
input = sys.stdin.readline


word1 = list(input().rstrip())
word2 = list(input().rstrip())
n = len(word1)
m = len(word2)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        if word1[i] == word2[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1

max_length = 0
for i in range(n + 1):
    for j in range(m + 1):
        if max_length < dp[i][j]:
            max_length = dp[i][j]

print(max_length)