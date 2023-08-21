import sys
from collections import deque

def bfs():
    q = deque([(0, 0, 0, 0)])
    while q:
        x, y, flag, n = q.popleft()
        
        if x==h-1 and y==w-1:
            if flag:
                print(visited[x][y][1]-1)
            else:
                print(visited[x][y][0]-1)
            return 
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<h and 0<=ny<w and board[nx][ny]==0:
                if not visited[nx][ny][0] or visited[nx][ny][2]>n:  #더 적은 jump로 갈 수 있다면
                    q.append((nx, ny, 0, n))
                    visited[nx][ny][2]=n
                    if flag:
                        visited[nx][ny][0]=visited[x][y][1]+1
                    else:
                        visited[nx][ny][0]=visited[x][y][0]+1
                        
        if n<k:
            for i in range(8):
                nx = x+mdx[i]
                ny = y+mdy[i]
                if 0<=nx<h and 0<=ny<w and board[nx][ny]==0:
                    if not visited[nx][ny][1] or visited[nx][ny][2]>n+1:
                        q.append((nx, ny, 1, n+1))
                        visited[nx][ny][2]=n+1
                        if flag:
                            visited[nx][ny][1]=visited[x][y][1]+1
                        else:
                            visited[nx][ny][1]=visited[x][y][0]+1
    print(-1)
    return

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
mdx = [-2, -1, 1, 2, 1, 2, -1, -2]
mdy = [1, 2, 2, 1, -2, -1, -2, -1]

k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
visited = [[[0, 0, 0] for _ in range(w)] for _ in range(h)]
visited[0][0] = [1, 1, 0]  #jump x, jump o, 횟수
bfs()