import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

seq = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


dp = [[None] * m for _ in range(n)]
dp[0][0] = seq[0]


def find(i, p):
    print(i)
    if dp[i][p] != None:
        return dp[i][p]

    max_p = -float("inf")
    max_index = None
    for j in range(i - 2, -1, -1):
        if find(j, p - 1) > max_p:
            max_p = find(j, p - 1)
            max_index = j

    if max_index != None:
        dp[i][p] = max(find(i - 1, p), find(j, p - 1))
    else:
        dp[i][p] = find(i - 1, p)

    return dp[i][p]


print(find(n - 1, m - 1))
