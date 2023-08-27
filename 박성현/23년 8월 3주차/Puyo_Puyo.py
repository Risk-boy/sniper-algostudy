import sys 
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

'''
1. 모든 12*6의 좌표에 대해 . 이 아니라면 
2. dx, dy를 이용해 bfs를 돌리고 
3. 만약 4개 이상 연결되어 있다면 해당 좌표들을 어딘가에 저장하기 ( 이 좌표들을 지우면서 +1 을 해줘야 1연쇄 취급)
3-1. tmp로 저장해두고 tmp 그룹을 '어딘가'에 저장하기
4. 저장된 만큼 graph 초기화 시켜주기
5. 이때 visited도 초기화시켜준다.
'''



def bfs(x,y,graph):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    start = graph[x][y]
    visited = [[0]*6 for _ in range(12)] #이거 False로 하는거랑 속도 차이 있나?
    queue = deque([(x,y)])
    group = [(x,y)]
    visited[x][y] = 1 

    while queue:
        x, y = queue.popleft() 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy 
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny] == start:
                queue.append((nx, ny))
                group.append((nx,ny))
                visited[nx][ny] = True
    return group

def delete_group(graph):
    deleted_group = []
    for x in range(12):
        for y in range(6):
            if graph[x][y] != '.':
                group = bfs(x,y,graph)
                if len(group)>=4:
                    deleted_group.extend(group)
    for x,y in deleted_group:
        graph[x][y] = '.'
    
    return len(deleted_group) > 0

def gravity(graph):
    for y in range(6):
        column = [graph[x][y] for x in range(12) if graph[x][y] != '.']
        for x in range(12-len(column)):
            graph[x][y] = '.'
        for x in range(12-len(column),12):
            graph[x][y] = column[x-(12-len(column))]

def sol(graph):
    chain = 0 
    while delete_group(graph):
        gravity(graph)
        chain += 1 
    return chain

initial_graph = [list(input()) for _ in range(12)]
print(sol(initial_graph))

