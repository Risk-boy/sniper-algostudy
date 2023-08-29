import sys 
from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]

virus = []

# 우선 바이러스를 놓을 수 있는 위치를 저장 후 해당 위치를 0으로 처리
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append([i,j])
            graph[i][j] = 0

def check():
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                return False
    return True

time = float('inf')

for comb in combinations(virus, M): # virus를 놓을 위치를 M개 조합으로 뽑아서
    visited = [row.copy() for row in graph]
    q = deque()

    # 우선 바이러스의 방문처리를 해준다.
    for x, y in comb: 
        visited[x][y] = 1 
        q.append((x,y,0))

    while q:
        x, y, count = q.popleft()
        if count >= time:
            break
        for dx, dy in directions:
            nx, ny = x+dx, y+dy 
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] != 1 :
                visited[nx][ny] = 1
                q.append((nx,ny,count+1))
    if check():
        time = min(time, count)
    
print(time) if time != float("inf") else print(-1)