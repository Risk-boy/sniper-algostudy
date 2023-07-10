from collections import defaultdict

import sys 
def input():
    return sys.stdin.readline().rstrip()

num_of_edges, start_water = map(int, input().split())
edges = []
for _ in range(num_of_edges-1):
    a, b = map(int, input().split())
    edges.append((a,b))

def solve(n, edges, root_id):
    global start_water
    graph = defaultdict(list)
    parent = [0]*(n+1)
    children = defaultdict(list)
    water = [0]*(n+1)
    visited = [0]*(n+1)
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    water[root_id] = start_water

    # define parent and children
    stack = [root_id]
    while stack:
        node = stack.pop()
        visited[node] = 1
        for child in graph[node]:
            if visited[child] == 0:
                parent[child] = node
                children[node].append(child)
                stack.append(child)

    # distribute water
    stack = [root_id]
    while stack:
        node = stack[-1]
        if water[node] > len(children[node]) and children[node]:
            distribute = water[node] / len(children[node])
            for child in children[node]:
                water[child] += distribute
                stack.append(child)
            water[node] = 0
        else:
            stack.pop()
            
    return round(sum(water) / len([w for w in water if w > 0]), 10)


print(solve(num_of_edges, edges, 1))