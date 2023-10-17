import sys
from collections import deque

def combi(i, select, sn, yn):
    if yn >= 4:
        return
    
    if len(select) == 7:
        if sn >= 4:
            path.append(select[:])
        return
    
    if len(select) >= 5 and sn <= 1:
        return
    
    for j in range(i, 25):
        select.append(pos[j])
        x, y = pos[j]
        combi(j + 1, select, sn + (board[x][y] == "S"), yn + (board[x][y] == "Y"))
        select.pop()
    
def bfs(x, y):
    q = deque([(x, y)])
    visit[p[0]] = 1
    
    while q:
        x, y = q.pop()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if visit.get((nx, ny), -1) < 0:
                continue
            if visit[(nx, ny)] == 0:
                visit[(nx, ny)] = 1
                q.append((nx, ny))
                
    if sum(visit.values()) == 7:
        return True
    return False

input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(5)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pos = [(i, j) for i in range(5) for j in range(5)]
path = []
answer = 0

combi(0,[], 0, 0)
for p in path:
    visit = {pos : 0 for pos in p}
    if bfs(*p[0]):
        answer += 1
        
print(answer)