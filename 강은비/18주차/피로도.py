import sys

d, w, r, m = map(int, sys.stdin.readline().split())
t, answer = 0, 0

for _ in range(24):
    if t+d<=m:
        t+=d
        answer+=w
    else:
        t-=r
        if t<0:
            t=0
            
print(answer)