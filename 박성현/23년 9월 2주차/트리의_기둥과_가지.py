from collections import defaultdict, deque
import sys 
def input():
    return sys.stdin.readline().rstrip()

N, R = map(int, input().split())
edges = defaultdict(list)
distances = defaultdict(int)

for _ in range(N - 1):
    a, b, d = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
    distances[(a, b)] = d
    distances[(b, a)] = d

def bfs_to_find_giga_and_pillar_length(start):
    visited = set()
    queue = deque([(start, 0)])
    deepest_leaf = None
    max_depth = 0
    
    while queue:
        node, length = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        unvisited_children = [child for child in edges[node] if child not in visited]
        
        if len(unvisited_children) >= 2:
            return node, length

        # 최초로 자식 노드가 없는 노드를 가장 깊은 리프 노드로 설정
        if not unvisited_children and length > max_depth:
            max_depth = length
            deepest_leaf = node

        for child in edges[node]:
            queue.append((child, length + distances[(node, child)]))

    return deepest_leaf, max_depth

def find_max_branch_length(giga):
    visited = set()
    queue = deque([(giga, 0)])
    max_length = 0

    while queue:
        node, length = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if len(edges[node]) == 1 and node != giga:
            max_length = max(max_length, length)

        for child in edges[node]:
            queue.append((child, length + distances[(node, child)]))

    return max_length

giga, pillar_length = bfs_to_find_giga_and_pillar_length(R)

# 리프노드가 1개뿐이라면, 기가노드에서 나머지 가지까지의 길이의 최댓값은 0이다.
if len(edges[giga]) == 1:
    branch_length = 0
else:
    branch_length = find_max_branch_length(giga)

print(pillar_length, branch_length)