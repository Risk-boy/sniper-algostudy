import sys
from itertools import combinations
from collections import deque

def move():
    global enemy_
    
    new = dict()
    for x, y in enemy_:
        if x+1<n:
            new[(x+1, y)] = 1
    enemy_ = new

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visit = set()
    
    while q:
        x, y = q.popleft()
        rx, ry = 16, 16
        for dx, dy in dir:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m and abs(nx-sx)+abs(ny-sy)<=d and not visit&set([(nx, ny)]):
                if enemy_.get((nx, ny), 0):
                    if ny<ry:
                        rx, ry = nx, ny
                else:
                    q.append((nx, ny))
                    visit.add((nx, ny))
                    
        if rx<16 and ry<16:
            return (rx, ry)
    return 
                
def attack(pos):
    global cnt, enemy_
    
    removed = set()
    for k in range(3):
        res = bfs(n, pos[k])
        if res:
            removed.add(res)
    cnt += len(removed) 
    for x, y in removed:
        enemy_.pop((x, y))
    
n, m, d= map(int, sys.stdin.readline().split())
enemy = dict()
board = []
dir = [(0, -1), (-1, 0), (0, 1)]
for i in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    board.append(x)
    for j in range(m):
        if x[j] == 1:
            enemy[(i, j)] = 1
                  
answer = -1
for c in combinations(range(m), 3):
    cnt = 0
    enemy_ = enemy.copy()
    while enemy_:
        attack(c)
        move()
    answer = max(answer, cnt)
    
print(answer)
        
    