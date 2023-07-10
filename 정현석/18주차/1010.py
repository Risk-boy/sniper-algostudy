import sys
from math import comb

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    [n, m] = map(int, sys.stdin.readline().split())
    print(comb(m, n))