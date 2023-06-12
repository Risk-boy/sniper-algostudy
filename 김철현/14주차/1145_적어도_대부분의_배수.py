import sys
input = sys.stdin.readline 
import math 
from itertools import combinations 


arr = list(map(int, input().split()))
min_v = 1000000
for a, b, c in combinations(arr, 3):
    lcm = math.lcm(a, b, c)
    if min_v > lcm:
        min_v = lcm

print(min_v)