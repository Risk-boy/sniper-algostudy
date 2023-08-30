import sys
input = sys.stdin.readline 
from collections import deque


def push(r, c, direction):
    global score
    idx = dict[direction]
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        if not visited[r][c]:
            visited[r][c] = True
            score += 1 
        k = arr[r][c]
        for _ in range(k - 1):
            r += dr[idx]
            c += dc[idx]
            if r < 0 or r >= n or c < 0 or c >= m:
                break
            if not visited[r][c]:
                q.append((r, c))
                visited[r][c] = True
                score += 1
            
            
n, m, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dict = {"E": 0, "W": 1, "S": 2, "N": 3}
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
score = 0
for _ in range(R):
    x, y, d = input().split()
    x = int(x) - 1
    y = int(y) - 1
    if not visited[x][y]:
        push(x, y, d)
    x, y = map(int, input().split())
    visited[x - 1][y - 1] = False

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            visited[i][j] = "F"
        else:
            visited[i][j] = "S"

print(score)
for row in visited:
    print(*row)