# 그리디
# 정렬

import sys

n = int(input())
dairy = []
for _ in range(n):
    c = int(sys.stdin.readline())
    dairy += [c]

dairy.sort(reverse=True)

price = 0
for idx, i in enumerate(dairy):
    if idx%3!=2:
        price += i

print(price)