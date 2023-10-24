import sys

sys.setrecursionlimit(10**8)

def dfs(s):
    global cnt 
    
    if len(s) == 0:
        cnt += 1
        return 
    
    dfs(s[:-1])
    if s[:-1] == s[1:]:
        return 
    dfs(s[1:])

n = list(sys.stdin.readline().rstrip())
cnt = 0
dfs(n)
print(cnt)
