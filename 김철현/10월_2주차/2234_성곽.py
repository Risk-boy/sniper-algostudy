import sys
input = sys.stdin.readline 
from collections import deque


def bfs(i, j):
    global idx
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt = 0
    while q:
        r, c = q.popleft()
        same_area[r][c] = idx
        cnt += 1
            
        temp = bin(16 ^ arr[r][c])[3:]
        temp = temp[::-1]
        for k in range(4):
            if temp[k] == "1":
                continue
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True
    
    room_area.append(cnt)
    idx += 1
    return cnt


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

room = 0
max_area = 0
visited = [[False] * M for _ in range(N)]
idx = 0
room_area = []
same_area = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            area = bfs(i, j)
            room += 1
            if max_area < area:
                max_area = area


max_union_area = 0
for r in range(N):
    for c in range(M):
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if same_area[r][c] != same_area[nr][nc]:
                    temp = room_area[same_area[r][c]] + room_area[same_area[nr][nc]]
                    if max_union_area < temp:
                        max_union_area = temp

print(room)
print(max_area)
print(max_union_area)