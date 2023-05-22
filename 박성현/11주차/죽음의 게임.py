import sys 
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

graph = []
for _ in range(N):
    graph.append([])
for i in range(N):
    graph[i].append(int(input()))
        
start = 0
cnt = 0
while start != K:
    if cnt == N:
        break
    else:
        start = graph[start][0]
        cnt += 1
if cnt == N:
    print(-1)
else:
    print(cnt)