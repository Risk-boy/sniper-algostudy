# 브루트포스

import sys
from itertools import combinations

n = int(input())

m = []
for _ in range(n):
    s, b = map(int, sys.stdin.readline().split())
    m += [(s, b)]

min_diff = 10000000000000
for i in range(1, len(m)+1):
    for j in combinations(m, i):
        sour = 1
        bitter = 0
        for k in j:
            sour *= k[0]
            bitter += k[1]
        diff = abs(sour-bitter)

        if diff < min_diff:
            min_diff = diff

print(min_diff)