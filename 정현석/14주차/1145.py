import sys
from itertools import combinations
from math import lcm

nums = list(map(int, sys.stdin.readline().rstrip().split()))

combs = list(combinations(nums, 3))
min_lcm = lcm(*combs[0])

for c in combs[1:]:
    min_lcm = min(min_lcm, lcm(*c))
    
print(min_lcm)