import sys
def input():
    return sys.stdin.readline().rstrip() 

def dfs(node, parent, order, low, adj_list, visited, is_cut_vertex):
    visited[node] = True
    order[node] = dfs.current_order
    low[node] = dfs.current_order
    dfs.current_order += 1
    child_count = 0
    
    for next_node in adj_list[node]:
        if not visited[next_node]:
            child_count += 1
            dfs(next_node, node, order, low, adj_list, visited, is_cut_vertex)
            low[node] = min(low[node], low[next_node])

            # 단절점 판별
            if parent != -1 and low[next_node] >= order[node]:
                is_cut_vertex[node] = True
        elif next_node != parent:
            low[node] = min(low[node], order[next_node])
    
    # 루트 노드 판별
    if parent == -1 and child_count > 1:
        is_cut_vertex[node] = True

N = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

order = [0] * (N+1)
low = [0] * (N+1)
visited = [False] * (N+1)
is_cut_vertex = [False] * (N+1)

dfs.current_order = 0
dfs(1, -1, order, low, adj_list, visited, is_cut_vertex)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        print("yes" if is_cut_vertex[k] else "no")
    else:
        print("yes")  # 트리에서 모든 간선은 단절선