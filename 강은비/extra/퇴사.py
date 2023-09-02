import sys

n = int(sys.stdin.readline())
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
p = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    ti, pi = schedule[i]
    if i+ti>n:
        p[i] = p[i+1]
    else:
        p[i] = max(p[i+1], p[ti+i]+pi)

print(p[0])