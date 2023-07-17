# 수학
# 구현
# 그리디

import sys

a, b, c, m = map(int, sys.stdin.readline().split())

work = 0
fatigue = 0
hour = 0

while hour!=24:
    if fatigue+a <= m:
        work += b
        fatigue += a
        hour += 1
    else:
        fatigue -= c
        hour += 1
        if fatigue < 0:
            fatigue = 0

print(work)