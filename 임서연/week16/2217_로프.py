# 그리디 알고리즘
# 정렬
# 문제 이해를 잘 해야됨

import sys

n = int(input())

weight = []
for i in range(n):
    w = int(sys.stdin.readline().rstrip())
    weight += [w]

weight.sort()

wt = 0
for idx, j in enumerate(weight):
    if wt < j:
        weight += [j*(n-idx)]

weight.sort()
print(weight[-1])