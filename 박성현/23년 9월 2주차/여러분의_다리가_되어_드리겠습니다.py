import sys
def input():
    return sys.stdin.readline().rstrip()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
parent = [i for i in range(N+1)]

for _ in range(N-2):
    a, b = map(int, input().split())
    union(parent, a, b)

group_set = set()
for i in range(1, N+1):
    group_set.add(find_parent(parent, i))

# 두 그룹 중 하나의 섬씩 연결
groups = list(group_set)
print(groups)
print(groups[0], groups[1])