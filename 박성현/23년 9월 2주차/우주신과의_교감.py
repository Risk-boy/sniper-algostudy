import math
import sys 

def input():
    return sys.stdin.readline().rstrip() 

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 모든 노드에 대한 좌표값 입력 받기
x = []
y = []
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append(data[0])
    y.append(data[1])

# 모든 간선의 길이를 계산하여 edges에 추가
for i in range(n):
    for j in range(i + 1, n):
        cost = distance(x[i], y[i], x[j], y[j])
        edges.append((cost, i + 1, j + 1))

# 이미 연결된 통로가 있다면 Union 연산 수행
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print("{:.2f}".format(result))