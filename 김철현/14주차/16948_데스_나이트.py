import sys
input = sys.stdin.readline 
from collections import deque 


def bfs():
    global r1, c1, r2, c2
    q = deque()
    q.append((r1, c1, 0))
    visited[r1][c1] = True
    
    while q:
        r, c, cnt = q.popleft()
        if r == r2 and c == c2:
            return cnt 
        
        for k in range(6):
            nr, nc = r + dr[k], c + dc[k]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, cnt + 1))
    return -1


n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]
visited = [[False] * n for _ in range(n)]
print(bfs())