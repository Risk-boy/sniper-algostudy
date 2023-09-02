import sys
from pprint import pprint
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip()

N,M,K = map(int,input().split())
graph = [[0]*M for _ in range(N)]

for _ in range(K):
    lr,lc,rr,rc = map(int,input().split())
    nr = rr-lr
    nc = rc-lc
    for r in range(nr):
        for c in range(nc):
            graph[lc+c][lr+r] += 1 


visited =[[False]*M for _ in range(N)]
areas = []
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x, y, cnt):
    if x < 0 or x >= N or y < 0 or y >= M:
        return cnt
    if visited[x][y] or graph[x][y] >= 1:
        return cnt
    
    visited[x][y] = True
    
    cnt += 1
    for dx, dy in directions:
        cnt = dfs(x + dx, y + dy, cnt)
        
    return cnt

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 0:
            areas.append(dfs(i, j, 0))

print(len(areas))
print(" ".join(map(str, sorted(areas))))

