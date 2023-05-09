import sys

n=int(sys.stdin.readline())
glass=[int(sys.stdin.readline()) for _ in range(n)]

dp=[[0 for _ in range(n+1)] for _ in range(3)] 

for i in range(1, n+1):
    if glass[i-1]>0:
        dp[0][i]=max(dp[0][i-1], dp[1][i-1], dp[2][i-1]) #마시지 않을때: 이전 단계의 최대 값
        dp[1][i]=dp[0][i-1]+glass[i-1]  #안마시고 마실때 : 이전 단계에서 안마셨을 때 + 현재 양
        dp[2][i]=dp[1][i-1]+glass[i-1]  #마시고 또 마실때 : 이전 단계에서 마셨을 때 + 현재 양
    else:
        dp[0][i]=dp[1][i]=dp[2][i]=max(dp[0][i-1], dp[1][i-1], dp[2][i-1])  #마시지 않을 때와 같음 
        
print(max(map(max, dp)))