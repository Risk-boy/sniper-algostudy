import sys

n, k, q=map(int, sys.stdin.readline().split())
s=list(map(int, sys.stdin.readline().split()))
qs=list(map(int, sys.stdin.readline().split()))

dp=[0 for _ in range(n+1)]
total=0

for i in range(n):
    if s[i]==k:
        dp[i+1]=dp[i]
        total=0
    else:
        total+=1
        dp[i+1]=dp[i]+total
        
for x in qs:
    print(dp[x])

