import sys
input = sys.stdin.readline 
from collections import deque


n, m, t = map(int, input().split())
arr = [[0] * m] + [deque(list(map(int, input().split()))) for _ in range(n)]

for _ in range(t):
    x, d, k = map(int, input().split())
    if d == 1:
        k = -k
    for idx in range(1, n + 1):
        if idx % x == 0:
            arr[idx].rotate(k)
    q = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r in range(1, n + 1):
        for c in range(m):
            if arr[r][c]:
                for _ in range(4):
                    nr, nc = r + dr[_], (c + dc[_]) % m
                    if 1 <= nr <= n and 0 <= nc < m:
                        if arr[r][c] == arr[nr][nc]:
                            q.append((r, c))
                            break

    if q:
        while q:
            r, c = q.pop()
            arr[r][c] = 0
    else:
        total = 0
        cnt = 0

        for i in range(1, n + 1):
            for j in range(m):
                if arr[i][j]:
                    total += arr[i][j]
                    cnt += 1
        mean = 0
        if cnt:
            mean = total / cnt
            for i in range(1, n + 1):
                for j in range(m):
                    if arr[i][j]:
                        if arr[i][j] > mean:
                            arr[i][j] -= 1
                        elif arr[i][j] < mean:
                            arr[i][j] += 1
        else:
            break
answer = 0
for i in range(1, n + 1):
    answer += sum(arr[i])

print(answer)