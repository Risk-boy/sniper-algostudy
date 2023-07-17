# 구현
# 시뮬레이션

import sys

n, m = map(int, sys.stdin.readline().split())
status = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if a==1:
        status[b-1] = c
    elif a==2:
        status[b-1:c] = [~x+2 for x in status[b-1:c]]
    elif a==3:
        status[b-1:c] = [0]*(c-b+1)
    elif a==4:
        status[b-1:c] = [1]*(c-b+1)

for i in status:
    print(i, end=' ')