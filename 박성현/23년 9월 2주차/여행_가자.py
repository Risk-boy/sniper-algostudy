def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, N+1):
        if data[j-1] == 1:
            union(parent, i, j)

plan = list(map(int, input().split()))

result = True
for i in range(M-1):
    if find(parent, plan[i]) != find(parent, plan[i+1]):
        result = False
        break

if result:
    print("YES")
else:
    print("NO")