import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()

# 하나를 3만큼 줄이거나 두 개를 각각 (1,2) 또는 (2,1) 씩 줄이거나.

N = int(input())
target = list(map(int,input().split()))

if N==1:
    if target[0]%3 == 0:
        print('YES')
    else:
        print('NO')

if N>=2:
    cnt = 0 
    if sum(target)%3 == 0:
        for tree in target:
            cnt += tree // 2
        if cnt >= (sum(target) // 3):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
    
