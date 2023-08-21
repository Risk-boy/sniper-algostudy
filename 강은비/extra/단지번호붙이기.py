import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+d[i][0]
            ny = y+d[i][1]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and board[nx][ny] == "1":
                q.append((nx, ny))
                visit[nx][ny] = 1
                cnt+=1
    return cnt
            
        
n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = []
for i in range(n):
    for j in range(n):
        if not visit[i][j] and board[i][j] == "1":
            visit[i][j] = 1
            answer.append(bfs(i, j))
            
print(len(answer))
answer.sort()
for x in answer:
    print(x)

