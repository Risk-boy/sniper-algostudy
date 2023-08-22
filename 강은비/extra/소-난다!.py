import sys

def dfs(i, d):
    if d == m:
        k = sum(x)
        if p[k]:
            answer.add(k)
        return
    
    for k in range(i, n):
        x[d] = h[k]
        dfs(k+1, d+1)
        x[d] = 0

n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
answer = set()
M = max(h)*m+1
p = [1 for _ in range(M)] 
for i in range(2, int(M**0.5)+1):
    if p[i]:
        for j in range(2*i, M, i):
            p[j] = 0
p[0] = p[1] = 0  #0, 1 제외
x = [0 for _ in range(m)]
dfs(0, 0)
answer = list(answer)
answer.sort()
if answer: 
    print(*answer)
else:
    print(-1)