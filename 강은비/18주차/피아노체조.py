import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
dp = [0 for _ in range(n)]

for i in range(n-1):
    if m[i]>m[i+1]:
        dp[i+1]=dp[i]+1
    else:
        dp[i+1] = dp[i] 
        
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    print(dp[y-1]-dp[x-1])
    