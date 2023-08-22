import sys
input = sys.stdin.readline 
from collections import deque


def check(x, y):
    result = [(x, y)]
    visited = [[False] * 6 for _ in range(12)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    color = arr[x][y]
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < 12 and 0 <= nc < 6:
                if arr[nr][nc] == color and not visited[nr][nc]:
                    result.append((nr, nc))
                    q.append((nr, nc))
                    visited[nr][nc] = True
                    
    if len(result) >= 4:
        return result
    else:
        return []                
                
                
arr = [list(input().rstrip()) for _ in range(12)]
answer = 0
while True:
    bomb = set()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != ".":
                for x in check(i, j):
                    bomb.add(x)

    if bomb:
        answer += 1
        for i, j in bomb:
            arr[i][j] = "."

        for i in range(11, -1, -1):
            for j in range(5, -1, -1):
                if arr[i][j] != ".":
                    for k in range(11, i - 1, -1):
                        if arr[k][j] == ".":
                            arr[k][j] = arr[i][j]
                            arr[i][j] = "."
                            break

    else:
        break

print(answer)