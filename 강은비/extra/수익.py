import sys

while True:
    n = int(sys.stdin.readline())
    if n ==0 :
        break
    
    p = [int(sys.stdin.readline()) for _ in range(n)]
    
    dp = [0 for _ in range(n)]
    dp[0] = p[0]
    
    for i in range(1, n):
        dp[i] = max(dp[i-1]+p[i], p[i])
        
    print(max(dp))