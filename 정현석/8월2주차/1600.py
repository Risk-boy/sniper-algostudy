import sys
from collections import deque

init_k = int(sys.stdin.readline().rstrip())

w, h = map(int, sys.stdin.readline().rstrip().split())

board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
board_visited = [[[0] * (init_k + 1) for _ in range(w)] for _ in range(h)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
hores_directions = [
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
]

if w == 1 and h == 1:
    min_move = 0
else:
    min_move = float("inf")

    q = deque([(0, 0, init_k, 0)])

    while q:
        x, y, k, move = q.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx == h - 1 and ny == w - 1:
                min_move = min(min_move, move + 1)
                continue

            if nx >= 0 and nx < h and ny >= 0 and ny < w and not board[nx][ny]:
                if not board_visited[nx][ny][k]:
                    board_visited[nx][ny][k] = move + 1
                    q.append((nx, ny, k, move + 1))
                else:
                    if move + 1 < board_visited[nx][ny][k]:
                        board_visited[nx][ny][k] = move + 1
                        q.append((nx, ny, k, move + 1))

        if k:
            for dx, dy in hores_directions:
                nx = x + dx
                ny = y + dy

                if nx == h - 1 and ny == w - 1:
                    min_move = min(min_move, move + 1)
                    continue

                if nx >= 0 and nx < h and ny >= 0 and ny < w and not board[nx][ny]:
                    if not board_visited[nx][ny][k - 1]:
                        board_visited[nx][ny][k - 1] = move + 1
                        q.append((nx, ny, k - 1, move + 1))
                    else:
                        if move + 1 < board_visited[nx][ny][k - 1]:
                            board_visited[nx][ny][k - 1] = move + 1
                            q.append((nx, ny, k - 1, move + 1))

print(min_move) if min_move != float("inf") else print(-1)
