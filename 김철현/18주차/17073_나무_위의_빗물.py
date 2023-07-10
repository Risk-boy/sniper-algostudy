import sys
input = sys.stdin.readline
from collections import deque


def solve():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        cur = q.popleft()
        children = []
        for node in graph[cur]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                children.append(node)

        if children:
            for child in children:
                water[child] += water[cur] / len(children)
            water[cur] = 0
    return


n, w = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
water = [0] * (n + 1)
water[1] = w
solve()
total = 0
cnt = 0
for i in range(1, n + 1):
    if water[i]:
        total += water[i]
        cnt += 1

print(total / cnt)










