import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque

def solve(i, j):
    q = deque()
    q.append((i, j))
    union = []
    total = 0
    while q:
        r, c = q.popleft()
        union.append((r, c))
        total += arr[r][c]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                    q.append((nr, nc))
                    visited[nr][nc] = True

    avg = total // len(union)
    for r, c in union:
        arr[r][c] = avg
    return len(union)


N, L, R = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0

while True:
    check = False
    visited=[[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = True
                if solve(r, c) > 1:
                    check = True
    if not check:
        break
    else:
        cnt += 1

print(cnt)