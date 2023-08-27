import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start, visited, graph):
    queue = deque([start])
    visited[start] = True
    edges = 0
    vertices = 0
    
    while queue:
        curr = queue.popleft()
        vertices += 1
        for neighbor in graph[curr]:
            edges += 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return vertices, edges // 2

def solution():
    case = 0
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        case += 1
        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        tree_count = 0
        for i in range(1, n+1):
            if not visited[i]:
                vertices, edges = bfs(i, visited, graph)
                if vertices - 1 == edges:
                    tree_count += 1
        
        if tree_count == 0:
            print(f"Case {case}: No trees.")
        elif tree_count == 1:
            print(f"Case {case}: There is one tree.")
        else:
            print(f"Case {case}: A forest of {tree_count} trees.")

solution()