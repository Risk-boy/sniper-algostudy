import sys
from collections import deque
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip()

R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * C for _ in range(R)]

# 불과 시작 위치 초기화
fires = deque()
start = None

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'F':
            fires.append((i, j, 0))
        if graph[i][j] == 'J':
            start = (i, j, 0)

# BFS로 불과 J의 움직임을 동시에 시뮬레이션
queue = deque([start])
while queue or fires:
    # 불을 먼저 이동시킴. 그래야 J가 이동하면 안되는 위치가 미리 처리됨.
    for _ in range(len(fires)):
        x, y, t = fires.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                graph[nx][ny] = 'F'
                fires.append((nx, ny, t + 1))

    # J가 이동
    for _ in range(len(queue)):
        x, y, t = queue.popleft()
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            print(t + 1)
            sys.exit(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                graph[nx][ny] = 'J'
                queue.append((nx, ny, t + 1))

print("IMPOSSIBLE")