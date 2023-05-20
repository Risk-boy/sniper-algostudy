import sys

n, k=map(int, sys.stdin.readline().split())
idx=[0 for _ in range(n)]
for i in range(n):
    idx[i]=int(sys.stdin.readline())
    
m=1
i=0
while True:
    next=idx[i]
    i=next
    if next==k:
        print(m)
        break
    m+=1
    if m>n:
        print(-1)
        break
    