# 수학
# 브루트포스

import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))

def is_prime(n):
    if n==1:
        return False
    else:
        for i in range(2, int(n/2)+1):
            if n%i==0:
                return False
    return True

prime = []
pick = list(combinations(weight, m))
for i in pick:
    sums = sum(i)
    if is_prime(sums):
        prime.append(sums)

if len(prime)==0:
    print(-1)
else:
    prime = list(set(prime))
    prime.sort()
    print(*prime)
