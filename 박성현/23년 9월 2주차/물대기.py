import sys 
import heapq
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
# 우물을 파는 비용
required_direct = [int(input()) for _ in range(N)]

# 논 사이의 연결 비용
graph = [list(map(int, input().split())) for _ in range(N)]

edges = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            edges[i].append((j, graph[i][j]))

def prim():
    visited = [False] * N
    q = []
    
    # 모든 논에 대한 우물을 파는 비용 추가
    for idx, cost in enumerate(required_direct):
        heapq.heappush(q, (cost, idx))
    
    total_cost = 0
    while q:
        cost, node = heapq.heappop(q)
        
        if not visited[node]:
            visited[node] = True
            total_cost += cost
            
            for next_node, next_cost in edges[node]:
                if not visited[next_node]:
                    heapq.heappush(q, (min(next_cost, required_direct[next_node]), next_node))
                    
    return total_cost if all(visited) else float('inf')  # 모든 논을 방문했는지 확인

# 각 논을 시작점으로 설정하고 프림 알고리즘 실행
result = prim()
print(result)


