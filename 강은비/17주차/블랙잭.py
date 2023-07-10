import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

answer = -1
for c in combinations(cards, 3):
    t = sum(c)
    if t == m:
        print(t)
        break
    elif t<=m and t>answer:
        answer = t
else:
    print(answer)