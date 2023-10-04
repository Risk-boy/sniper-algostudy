import sys

def dfs(i):
    if i == n + 1:
        return 1
    return i * dfs(i + 1)

n = int(sys.stdin.readline())
print(str(dfs(1)).rstrip('0')[-1])
