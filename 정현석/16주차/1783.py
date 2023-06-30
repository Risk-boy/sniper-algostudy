import sys
from math import ceil

[n, m] = list(map(int, sys.stdin.readline().rstrip().split()))

def count_cells(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return min(4, ceil(m / 2))
    else:
        if m < 5:
            return m
        elif m == 5:
            return 4
        else:
            return m-2
        
print(count_cells(n, m))