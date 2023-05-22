import sys
import math

# 인터넷 보고 참고함

n = int(sys.stdin.readline().rstrip())
edges = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[math.inf] * (1 << n) for _ in range(n)]

def dfs(x, visited):
    if visited == (1 << n) - 1:
        if edges[x][0]:
            return edges[x][0]
        else:
            return math.inf

    if dp[x][visited] != math.inf:
        return dp[x][visited]

    for i in range(1, n):
        if not edges[x][i]:
            continue
        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + edges[x][i])
    return dp[x][visited]

print(dfs(0, 1))