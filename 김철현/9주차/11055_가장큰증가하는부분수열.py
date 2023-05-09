import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
dp = []
for num in arr:
    dp.append(num)

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]

print(max(dp))