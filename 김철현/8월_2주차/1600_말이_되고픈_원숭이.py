import sys
input = sys.stdin.readline 
from collections import deque


def bfs():
    visited[0][0][0] = 0
    q = deque()
    q.append((0, 0, 0))
    
    while q:
        r, c, cnt = q.popleft()
        
        # 일반 이동
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0:
                    if not visited[nr][nc][cnt]:
                        visited[nr][nc][cnt] = visited[r][c][cnt] + 1
                        q.append((nr, nc, cnt))

        
        # 말 이동
        if cnt < K:
            for k in range(8):
                nr, nc = r + hr[k], c + hc[k]
                if 0 <= nr < n and 0 <= nc < m:
                    if arr[nr][nc] == 0:
                        if not visited[nr][nc][cnt + 1]:
                            visited[nr][nc][cnt + 1] = True
                            visited[nr][nc][cnt + 1] = visited[r][c][cnt] + 1
                            q.append((nr, nc, cnt + 1))
        


K = int(input())
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

hr = [-2, -1, 1, 2, 2, 1, -1, -2]
hc = [1, 2, 2, 1, -1, -2, -2, -1]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[[0] * (K + 1) for _ in range(m)] for _ in range(n)]

bfs()
answer = m * n + 1
for x in visited[-1][-1]:
    if x != 0:
        if x < answer:
            answer = x

if m == 1 and n == 1:
    print(0)
    exit()
if answer != m * n + 1:
    print(answer)
else:
    print(-1)

