import sys
input = sys.stdin.readline 
from collections import deque 


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if not visited[nr][nc] and arr[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    
    return 


n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
for i in range(m):
    if not visited[0][i] and arr[0][i] == 0:
        bfs(0, i)

for i in range(m):
    if visited[n - 1][i]:
        print("YES")
        exit()

print("NO")
