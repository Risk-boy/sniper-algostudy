import sys
from collections import deque
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().rstrip()

row, col = map(int,input().split())
graph = []

for _ in range(row):
    graph.append(list(map(int,list(input()))))

dx, dy = [1,-1,0,0], [0,0,1,-1]

result = []

def bfs(a,b,graph):
    if graph[a][b]==1 or graph[a][b]==-1: # 시작할 수 없음
        return False
    queue = deque([(a,b)])
    while queue:
        x, y = queue.popleft()
        if graph[x][y]==0 and x==(row-1):
            return True
        if graph[x][y]!=0:
            continue
        graph[x][y]=-1 # 방문처리 
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<row and 0<=ny<col and graph[nx][ny]==0:
                queue.append((nx,ny))
    return False

result = 'NO'
for i in range(col-1):
    if bfs(0,i,graph):
        result = 'YES'
        break

print(result)
    

