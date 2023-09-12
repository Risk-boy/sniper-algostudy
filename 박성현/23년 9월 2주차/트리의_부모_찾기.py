import sys
from collections import deque 

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
graph = [[] for _ in range(N+1)] # 인덱스 i에는 자식들을 저장
parent = [0 for _ in range(N+1)] # 부모를 표시할 자료구조

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, graph, parent):
    q = deque([start])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if parent[i]==0 : #아직 부모가 없다면
                parent[i] = v 
                q.append(i)

bfs(1, graph, parent)

# 결과 출력
for i in range(2, N + 1):
    print(parent[i])