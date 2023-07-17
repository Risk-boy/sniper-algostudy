# 누적 합
# 시간 계산을 해야 함 O(N^2), O(N), O(1)

import sys

n = int(sys.stdin.readline().rstrip())
hard = list(map(int, sys.stdin.readline().split()))

miss = [0]*n
sum = 0
for i in range(1, n):
    if hard[i] < hard[i-1]:
        sum += 1
    miss[i] = sum

q = int(sys.stdin.readline().rstrip())
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    total = miss[y-1] - miss[x-1]
    print(total)