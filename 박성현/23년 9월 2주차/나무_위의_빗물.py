from collections import defaultdict, deque

N, W = map(int, input().split())
edges = defaultdict(list)

# 그래프 구성 (무방향 그래프로)
for _ in range(N-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# BFS를 사용하여 각 리프 노드까지의 경로의 노드 수 계산
queue = deque([(1, 0)])  # (노드 번호, 깊이)
visited = set()
leaf_nodes = []

while queue:
    node, depth = queue.popleft()
    if node in visited:
        continue
    visited.add(node)
    
    children = [child for child in edges[node] if child not in visited]
    
    if not children:  # 리프 노드라면
        leaf_nodes.append(node)
    else:
        for child in children:
            queue.append((child, depth + 1))

# 루트 노드에서 리프 노드까지의 경로에 따라 물이 분배됨.
# 모든 리프 노드들은 루트 노드에서의 물을 공히 나눠받기 때문에 평균은 전체 물의 양을 리프 노드의 수로 나눈 것과 같다.
answer = W / len(leaf_nodes)
print(answer)