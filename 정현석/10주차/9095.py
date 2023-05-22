import sys

t = int(sys.stdin.readline().rstrip())
n_list = [int(sys.stdin.readline().rstrip()) for _ in range(t)]

dp = {}
dp[1] = 1
dp[2] = 2
dp[3] = 4

def find_dp(n):
    if n in dp:
        return dp[n]
    else:
        dp[n] = find_dp(n-3) + find_dp(n-2) + find_dp(n-1)
        return dp[n]
            
for n in n_list:
    print(find_dp(n))