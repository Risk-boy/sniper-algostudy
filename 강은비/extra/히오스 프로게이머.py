import sys

input = sys.stdin.readline
n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]
l = min(x)
r = max(x) + k
answer = -1
while l <= r:
    mid = (l + r) // 2
    total = 0
    for xi in x:
        if mid > xi:
            total += mid - xi
            
    if total <= k:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1
        
print(answer)