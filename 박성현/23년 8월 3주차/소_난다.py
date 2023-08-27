import sys
import math
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def is_prime(N):
    if N < 2 :
        return False
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False 
    return True
    
N,M = map(int,input().split())
data = list(map(int,input().split()))
result = set()
for i in list(combinations(data, M)):
    tmp = sum(i)
    if is_prime(tmp):
        result.add(tmp)

if len(result)==0:
    print(-1)
else:
    print(*(sorted(list(result))))
