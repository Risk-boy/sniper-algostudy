import sys
input = sys.stdin.readline 


N, K = map(int, input().split())
arr = list(map(int, input().split()))
MOD = int(1e9) + 7


cnt = 0
for i in range(N - 1, -1, -1):
    if arr[i] != K:
        cnt = (cnt + pow(2, i, MOD) % MOD) % MOD
        K = 6 - K - arr[i]

print(cnt)