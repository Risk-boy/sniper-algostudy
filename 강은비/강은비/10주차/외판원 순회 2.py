import sys
from collections import deque

def dfs(x, s, visit):
    if x==s and all(visit):
        answer.append(visit[x])
        return

    for i, v in enumerate(w[x]):
        if not visit[i] and v:
            visit[i]=visit[x]+v
            dfs(i, s,visit)
            visit[i]=0
                
answer=[]
n=int(sys.stdin.readline())
w=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dfs(0, 0, [0 for _ in range(n)])
answer.sort()
print(answer[0])