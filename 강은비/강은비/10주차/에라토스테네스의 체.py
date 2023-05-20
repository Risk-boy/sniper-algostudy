import sys
from collections import deque

n, k=map(int, sys.stdin.readline().split())
nums=[1 for _ in range(n+1)]
cnt=0
p=2

while True:
    for j in range(p, n+1):
        if nums[j]==1:
            p=j
            break
        
    for x in range(2, n+1):
        if x%p==0 and nums[x]==1:
            cnt+=1
            nums[x]=0
        if cnt==k:
            print(x)
            sys.exit()
            