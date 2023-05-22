import sys

# n = int(sys.stdin.readline())
# seq = list(map(int, sys.stdin.readline().rstrip().split()))

n = 10
seq = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]

dp = seq.copy()

max_sum = dp[0]

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:
            new_sum = dp[j] + seq[i]
            if new_sum > dp[i]:
                dp[i] = new_sum
    if dp[i] > max_sum:
        max_sum = dp[i]

print(max_sum)