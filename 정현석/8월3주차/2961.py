import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())

i = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]


def find_diff(x, s, b):
    if x == n:
        if b != 0:
            return abs(s - b)
        else:
            return float("inf")

    cs, cb = i[x]

    return min(find_diff(x + 1, s * cs, b + cb), find_diff(x + 1, s, b))


print(find_diff(0, 1, 0))
