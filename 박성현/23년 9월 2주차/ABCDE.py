import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, depth, visited):
    if depth == 4:
        return True
    
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, depth + 1, visited):
                return True
    visited[node] = False
    
    return False

result = 0

for i in range(N):
    visited = [False] * N  # 새로운 visited 배열을 만들어야 합니다.
    if dfs(i, 0, visited):
        result = 1
        break

print(result)