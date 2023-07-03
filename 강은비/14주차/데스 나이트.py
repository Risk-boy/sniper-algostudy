import sys
from collections import deque

def bfs(sx, sy, d):
    dx=[-2, -2, 0, 0, 2, 2]
    dy=[-1, 1, -2, 2, -1, 1]
     
    q=deque([(sx, sy, d)])
    while q:
        x, y, d=q.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if nx==r and ny==c:
                    print(d+1)
                    sys.exit()
                q.append((nx, ny, d+1))
                visited[nx][ny]=1
    print(-1)

n=int(sys.stdin.readline())
sx, sy, r, c=map(int, sys.stdin.readline().split())
visited=[[0 for _ in range(n)] for _ in range(n)]
bfs(sx, sy, 0)
