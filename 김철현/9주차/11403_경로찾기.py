import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque


def bfs(s):
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()
        for node in graph[v]:
            if not visited[s][node]:
                visited[s][node] = 1
                q.append(node)


n = int(input())
graph = [[] for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:
            graph[i].append(j)

for k in range(n):
    bfs(k)

for ls in visited:
    print(*ls)
