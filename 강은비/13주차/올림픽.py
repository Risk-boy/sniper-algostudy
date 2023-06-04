import sys
from collections import defaultdict

n, k=map(int, sys.stdin.readline().split())
country=dict()
for _ in range(n):
    i, *x=list(map(int, sys.stdin.readline().split()))
    country[i]=x
country=dict(sorted(country.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2])))

rank=0
cnt=1
tmp=[]
for i, v in country.items():
    if tmp!=v:
        rank+=cnt
        tmp=v
        cnt=1
    else:
        cnt+=1
    if i==k:
        print(rank)
        break
    
    
    
    