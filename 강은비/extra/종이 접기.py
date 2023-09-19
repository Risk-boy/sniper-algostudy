import sys

def dfs(i, j):
    if i == j:
        return True
    
    mid = (i+j) // 2
    for k in range(1, mid - i + 1):
        if not int(s[mid - k]) ^ int(s[mid + k]):
            return False
    return dfs(i, mid) & dfs(mid + 1, j)
        
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    if dfs(0, len(s)):
        print("YES")
    else:
        print("NO")
    
        