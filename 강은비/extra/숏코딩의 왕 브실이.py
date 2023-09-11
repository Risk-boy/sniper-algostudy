import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
r = n - m - 1
l = 0
mini = a[l]
answer = a[r] - a[l]
while r <= n-1:
    if a[l] < mini:
        mini = a[l]
    if a[r] - mini > answer:
        answer = a[r] - mini
    l += 1
    r += 1

print(answer)
    