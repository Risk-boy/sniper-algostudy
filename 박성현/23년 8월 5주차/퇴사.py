import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()
N = int(input())
T = []
P = []
dp = [0] * (N+1)  

for _ in range(N):
    time, profit = map(int, input().split())
    T.append(time)
    P.append(profit)


for i in range(N-1, -1, -1):
    if i + T[i] > N:  
        dp[i] = dp[i+1]
    else:  
        dp[i] = max(dp[i+1], P[i] + dp[i+T[i]])

print(dp[0])