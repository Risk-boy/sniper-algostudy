import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

n_city, n_edge, K, start = map(int,input().split())

graph = [[] for _ in range(n_city + 1)]
visited = [False] * (n_city + 1)

for _ in range(n_edge):
    a, b = map(int,input().split())
    graph[a].append(b)

def bfs(start):
    result = []
    q = deque([(start, 0)])
    visited[start] = True

    
    while q :
        cur, dist = q.popleft()
        if dist == K:
            result.append(cur)
        
        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                q.append((i, dist + 1))
    return result

cities = bfs(start)

if cities:
    cities.sort()
    for city in cities:
        print(city)
else:
    print(-1)