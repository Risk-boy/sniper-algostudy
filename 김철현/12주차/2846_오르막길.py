import sys
input = sys.stdin.readline 


n = int(input())
arr = list(map(int, input().split()))

max_v = 0
min_h = arr[0]
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        max_v = max(arr[i] - min_h, max_v)
    else:
        min_h = arr[i]

print(max_v)