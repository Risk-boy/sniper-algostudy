import sys 
from collections import deque

sys.setrecursionlimit(10**5)

def input():
    return sys.stdin.readline().rstrip()

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# 방문 여부와 최대 거리를 저장하는 딕셔너리
memo = {}

# 이동 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# DFS 함수
def dfs(x, y, visited):
    if (x, y, visited) in memo:
        return memo[(x, y, visited)]

    max_count = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            next_char = board[nx][ny]
            if next_char not in visited:
                max_count = max(max_count, 1 + dfs(nx, ny, visited + next_char))

    memo[(x, y, visited)] = max_count
    return max_count

# DFS를 (0, 0)에서 시작
print(dfs(0, 0, board[0][0]))