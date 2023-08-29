import sys
input = sys.stdin.readline 
from itertools import combinations 
from collections import deque 


def solve(q):
    q = deque(q)
    
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] == -1 and arr[nr][nc] != 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
    
    return
    
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

ls = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ls.append((i, j))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
min_time = float("inf")

for virus in list(combinations(ls, m)):
    time = -1
    visited = [[-1] * n for _ in range(n)]
    for i, j in virus:
        visited[i][j] = 0
    solve(virus)
    check = False
    for i in range(n):
        if check:
            break
        for j in range(n):
            if arr[i][j] != 1 and visited[i][j] == -1:
                check = True
                break
            elif arr[i][j] != 1:
                time = max(visited[i][j], time)
    if not check and time != -1:
        min_time = min(min_time, time)

if min_time == float("inf"):
    print(-1)
else:
    print(min_time)