import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
arr = [["."] * (m + 2)]  + [["."] + list(input().rstrip()) + ["."] for _ in range(n)] + [["."] * (m + 2)]

land = []
for i in range(n + 2):
    for j in range(m + 2):
        if arr[i][j] == "X":
            land.append((i, j))

change = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for r, c in land:
    cnt = 0
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if arr[nr][nc] == ".":
            cnt += 1
    if cnt >= 3:
        change.append((r, c))

for r, c in change:
    arr[r][c] = "."

row = []
col = []
for i in range(n + 2):
    for j in range(m + 2):
        if arr[i][j] == "X":
            row.append(i)
            col.append(j)

for i in range(min(row), max(row) + 1):
    for j in range(min(col), max(col) + 1):
        print(arr[i][j], end="")
    print()