import sys
input = sys.stdin.readline 


n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
max_w = 0

for i in range(n):
    if arr[i] * (i + 1) > max_w:
        max_w = arr[i] * (i + 1)
    
print(max_w)