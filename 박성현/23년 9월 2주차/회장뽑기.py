from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

min_score = float('inf')
candidates = []

# Reuse visited and distance arrays
visited = [False] * (N + 1)
distance = [0] * (N + 1)

for i in range(1, N+1):
    # Reset visited and distance arrays
    for j in range(1, N + 1):
        visited[j] = False
        distance[j] = 0

    queue = deque([i])
    visited[i] = True
    
    early_exit = False
    while queue:
        if early_exit:
            break
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                if distance[neighbor] > min_score:
                    early_exit = True
                    break
                queue.append(neighbor)
    
    max_distance = max(distance[1:])
    if max_distance < min_score:
        min_score = max_distance
        candidates = [i]
    elif max_distance == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(" ".join(map(str, sorted(candidates))))