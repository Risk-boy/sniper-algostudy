import sys

[v, e] = list(map(int, sys.stdin.readline().rstrip().split()))

edges = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(e)]

for edge in edges:
    edge[0] -= 1
    edge[1] -= 1

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1


total = 0
i = 0
edge = 0
edges = sorted(edges, key=lambda item: item[2])
parent = list(range(v))
rank = [0] * v

while edge < v - 1:
    node_1, node_2, w = edges[i]
    i += 1
    x = find(parent, node_1)
    y = find(parent, node_2)

    if x != y:
        edge += 1
        total += w
        union(parent, rank, x, y)

print(total)