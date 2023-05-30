import sys

n=int(sys.stdin.readline())
p=list(map(int, sys.stdin.readline().split()))

dp=[0 for _ in range(n)]

for i in range(1, n):
    if p[i]>p[i-1]:
        dp[i]=(p[i]-p[i-1]+dp[i-1])
print(max(dp))
        
