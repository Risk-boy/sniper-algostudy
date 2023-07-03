import sys
input = sys.stdin.readline 
import math


n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    print(min(math.ceil(m / 2), 4))
else:
    print(max(min(m, 4), m - 2))
