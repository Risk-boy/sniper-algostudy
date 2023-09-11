import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_v = arr[N - M - 1] - arr[0]
min_v = arr[0]
idx = 1
for i in range(N - M, N):
    min_v = min(min_v, arr[idx])
    max_v = max(max_v, arr[i] - min_v)
    idx += 1
    
print(max_v)