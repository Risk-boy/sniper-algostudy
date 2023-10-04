import sys

def dfs(prev, cnt):
    global answer
    
    if cnt == n:
        answer += 1
        return
        
    for x in ch:
        if x == prev:
            continue
        
        if d[x] >= 1:
            d[x] -= 1
            dfs(x, cnt + 1)
            d[x] += 1
        
s = sys.stdin.readline().rstrip()
d = {}
for x in s:
    d[x] = d.get(x, 0) + 1
    
ch = list(d.keys())
n = len(s)
answer = 0
dfs("", 0)

print(answer)
