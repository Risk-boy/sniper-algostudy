import sys
input = sys.stdin.readline 
from collections import defaultdict, deque


def check_time(i, j):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False] * N for _ in range(M)]
    visited[i][j] = True
    q = deque()
    q.append((i, j, 0))
    
    while q:
        r, c, t = q.popleft()
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc] and arr[nr][nc] != "X":
                    q.append((nr, nc, t + 1))
                    visited[nr][nc] = True
                    if arr[nr][nc] != ".":
                        time[t + 1].append(arr[nr][nc])
    
M, N, P = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(M)]
player = defaultdict(int)
for _ in range(P):
    name, dps = input().rstrip().split()
    player[name] = int(dps)

HP = int(input())
time = defaultdict(list)
for i in range(M):
    for j in range(N):
        if arr[i][j] == "B":
            check_time(i, j)

times = list(time.keys())
for t in times:
    temp = 0
    for p in time[t]:
        temp += player[p]
    time[t].append(temp)
    
cur_dps = time[times[0]][-1]
ans = len(time[times[0]]) - 1
for i in range(1, len(times)):
    interval_time = times[i] - times[i - 1]
    HP -= cur_dps * interval_time
    if HP <= 0:
        break
    
    cur_dps += time[times[i]][-1]
    ans += len(time[times[i]]) - 1

print(ans)