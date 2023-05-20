import sys

n, k=map(int, sys.stdin.readline().split())
s=list(map(int, sys.stdin.readline().split()))

dp=[0 for _ in range(n)]
for i in range(n):
    if s[i]%2==0:
        dp[i]=1

for i in range(n):
    for j in range(i):
        if dp[j]%2==0:
            dp[i]+=1