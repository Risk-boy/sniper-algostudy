import sys
from math import ceil

n, a, b, c, d = map(int, sys.stdin.readline().split())
cost = float("inf")

if a/b < c/d:   
    for i in range(c):   #ac < db
        if n-a*i>0:  
            cost = min(cost, i*b+d*ceil((n-a*i)/c))
        else:
            cost = min(cost, i*b)

else:
    for i in range(a):   #ac >= db
        if n-c*i>0:
            cost = min(cost, i*d+b*ceil((n-c*i)/a))
        else:
            cost = min(cost, i*d)

print(cost)

