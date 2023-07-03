import sys

pos=dict()
cnt=0
n=int(sys.stdin.readline())
for _ in range(n):
    i, x=map(int, sys.stdin.readline().split())
    y=pos.get(i, -1)
    if y!=x:
        if y>=0:
            cnt+=1
        pos[i]=x
    
print(cnt)