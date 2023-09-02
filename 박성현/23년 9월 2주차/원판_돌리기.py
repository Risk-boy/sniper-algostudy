import sys 
from copy import deepcopy
from pprint import pprint

sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip() 


N,M,K = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]

# 단일 원판을 회전시키는 로직
def rotate(data:list, d, k):
    k = k % len(data)  # k가 리스트의 길이보다 클 경우를 대비하여 나머지를 구합니다.
    if d == 0:  # 시계 방향
        return data[-k:] + data[:-k]
    else:  # 반시계 방향
        return data[k:] + data[:k]

directions = [(0,1),(0,-1),(1,0),(-1,0)]    

# 같은 수들을 찾는 로직
def dfs(graph, visited, x, y, N, M):
    value = graph[x][y]
    group = [(x, y)]
    visited[x][y] = True
    
    for dx,dy in directions:
        nx,ny = x + dx, y + dy
    
        if nx < 0: continue
        if nx >= N: continue
        
        # 원판에서 좌, 우 끝이 연결되어 있을 때
        ny = ny % M

        if visited[nx][ny]: continue

        if graph[nx][ny] == value:
            visited[nx][ny] = True
            group.extend(dfs(graph, visited, nx, ny, N, M))

    return group

def find_same_value(graph):
    global N, M
    new_graph = deepcopy(graph)  # 깊은 복사를 통해 새로운 객체를 생성
    visited = [[False]*M for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                group = dfs(new_graph, visited, i, j, N, M)
                if len(group) > 1:
                    groups.append(group)
    # groups에 저장된 좌표들의 값을 0으로 바꾸기
    for group in groups:
        for x, y in group:
            new_graph[x][y] = 0
    return new_graph

# 평균을 구해서 더하고 빼는 로직
def average_value(graph):
    new_graph = deepcopy(graph)  # 깊은 복사를 통해 새로운 객체를 생성
    total_sum = 0
    total_count = 0
    for i in range(N):
        for j in range(M):
            if new_graph[i][j] != 0:
                total_sum += new_graph[i][j]
                total_count += 1

    if total_count == 0:
        return new_graph

    avg = total_sum / total_count

    for i in range(N):
        for j in range(M):
            if new_graph[i][j] > avg:
                new_graph[i][j] -= 1
            elif new_graph[i][j] < avg and new_graph[i][j] != 0:
                new_graph[i][j] += 1
    return new_graph

# 최종 아웃풋을 위한 로직
def sum_remaining_values(graph):
    total_sum = 0
    for row in graph:
        total_sum += sum(row)
    return total_sum


for state in range(K):
    # print(f"state:{state} initial graph")
    # pprint(graph)
    circle, d, k = map(int,input().split())
    num_to_rotate = [i for i in range(1,N+1) if i % circle==0] # 회전시킬 서클 찾기
    # print(num_to_rotate)
    for idx in num_to_rotate:
        graph[idx-1] = rotate(graph[idx-1], d, k) # 회전시킨다.
    # print(f"state:{state} after rotate graph")
    # pprint(graph)
    new_graph = find_same_value(graph)
    if new_graph == graph:
        graph = average_value(new_graph)    
    else:
        graph = new_graph
    # print(f"state:{state} last graph")
    # pprint(graph)

print(sum_remaining_values(graph))



