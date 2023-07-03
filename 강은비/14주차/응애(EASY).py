import sys

n, m, k=map(int, sys.stdin.readline().split())
s=[0 for _ in range(n)]
for _ in range(m):
    s[int(sys.stdin.readline())]=1

for _ in range(k):
    t=[0 for _ in range(n)]      #다음에 인사할 사람
    for i in range(n):
        if s[(i-1)%n]+s[(i+1)%n]==1:
            t[i]=1
    s=t
    
print(sum(s))