def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M, k = map(int, input().split())
friend_cost = [0] + list(map(int, input().split()))

parent = [i for i in range(N+1)]

# 친구 관계를 통한 Union 연산
for _ in range(M):
    a, b = map(int, input().split())
    union_parent(a, b)

# 각 그룹별 최소 친구비
group_cost = {}
for i in range(1, N+1):
    root = find_parent(i)
    if root not in group_cost:
        group_cost[root] = friend_cost[i]
    else:
        group_cost[root] = min(group_cost[root], friend_cost[i])

# 총 비용 계산
total_cost = sum(group_cost.values())

if total_cost <= k:
    print(total_cost)
else:
    print("Oh no")