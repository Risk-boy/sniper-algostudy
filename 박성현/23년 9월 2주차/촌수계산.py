from collections import deque, defaultdict

def bfs(graph, parent, start, end):
    visited = [False] * (n+1)
    queue = deque([(start, 0)])
    
    while queue:
        curr, cnt = queue.popleft()
        visited[curr] = True

        if curr == end:
            return cnt
        
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                if parent[neighbor] == curr or parent[curr] == neighbor:  # 부모-자식 관계
                    queue.append((neighbor, cnt + 1))
                else:  # 형제 관계
                    queue.append((neighbor, cnt + 2))
                visited[neighbor] = True

    return -1  # 경로가 없는 경우

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = defaultdict(list)
parent = {i: None for i in range(1, n+1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    parent[y] = x

print(bfs(graph, parent, a, b))





