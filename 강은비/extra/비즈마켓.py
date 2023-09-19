import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a.sort()
b.sort(reverse=True)
answer = 0
idx = min(n, m)
for i in range(1, idx + 1):
    if a[n-i] - b[m-i] <= 0:
        break
    answer += a[n-i] - b[m-i]
    
print(answer)    