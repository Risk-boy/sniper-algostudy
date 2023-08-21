import sys

n, m = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        t[b-1] = c
    elif a == 2:
        t[b-1:c] = list(map(lambda x: x^1, t[b-1:c]))
    elif a == 3:
        t[b-1:c] = [0]*(c-b+1)
    else: 
        t[b-1:c] = [1]*(c-b+1)
print(*t)