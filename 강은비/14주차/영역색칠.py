import sys

n, m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt=0
for r in board:
    cnt1=0
    cnt2=0
    for i in range(m):
        if r[i]==1 and (r[i-1]!=1 or i==0):
            cnt1+=1
        elif r[i]==2 and (r[i-1]!=2 or i==0):
            cnt2+=1
        elif r[i]==0:
            cnt+=cnt1+cnt2
            cnt1=0
            cnt2=0
    cnt+=cnt1+cnt2
    
print(cnt)
