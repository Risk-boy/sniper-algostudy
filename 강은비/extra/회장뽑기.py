import sys
from collections import deque, defaultdict

def bfs(s):
    q = deque([s])
    while q:
        u = q.popleft()
        for x in edges[u]:
            if not visit[x]:
                q.append(x)
                visit[x] = visit[u]+1

n = int(sys.stdin.readline())
edges = defaultdict(list)
visit = [[-1 for _ in range(n)] for _ in range(n)]
score = [0 for _ in range(n)]
while True:
    x, y = map(int, sys.stdin.readline().split())
    if x == -1 and y == -1:
        break
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)
    
for i in range(n):
    visit = [0 for _ in range(n)]
    visit[i] = 1
    bfs(i)
    score[i] = max(visit)-1
 
m = min(score)

answer = []
for i in range(n):
    if score[i] == m :
        answer.append(i+1)
        
print(m, len(answer))
print(*answer)
        