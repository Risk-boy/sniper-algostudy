import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

K = int(input())
N,M = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
distance = [[0]*M for _ in range(N)]
direction = [[False,1,0],[False,-1,0],[False,0,1],[False,0,-1],[True, 2,1],[True, 2,-1],[True, -2,1],[True, -2,-1],[True, 1,2],[True, 1,-2],[True, -1,2],[True, -1,-2]]

def bfs():
    count = 0
    queue = deque()
    queue.append([0,0])
    distance[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for knight, dx, dy in direction:
            if knight:
                if count < K:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M: 
                        continue 
                    if distance[nx][ny]!=0:
                        continue
                    if graph[nx][ny] == 1 :
                        continue
                    distance[nx][ny] = min(distance[nx][ny],distance[x][y] + 1)
                    queue.append([nx,ny])
                    count += 1
                else:
                    continue
            else:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M: 
                    continue 
                if distance[nx][ny]!=0:
                    continue
                if graph[nx][ny] == 1 :
                    continue
                distance[nx][ny] = distance[x][y] + 1
                queue.append([nx,ny])
    print(distance[N-1][M-1])
bfs()
            