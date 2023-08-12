# 그리디
# 정렬

import sys

t = int(input())
for i in range(t):
    n = int(input())
    
    lb = []
    for j in range(n):
        p, i = map(int, sys.stdin.readline().split())
        lb += [(p, i)]
        if p==1:
            min_i = i
    lb.sort()

    cnt = 0
    for pp in lb:
        if pp[1] <= min_i:
            min_i = pp[1]
            cnt += 1

    print(cnt)