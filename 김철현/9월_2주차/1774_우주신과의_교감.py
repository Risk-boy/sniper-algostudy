import sys
input = sys.stdin.readline 


def find(x):
    if x != parent[x]:
        return find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent[y] = x
    elif x > y:
        parent[x] = y
    return

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


n, m = map(int, input().split())
arr = [0] + [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)
    
heap = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        heap.append((get_distance(arr[i][0], arr[i][1], arr[j][0], arr[j][1]), i, j))
ans = 0
heap.sort()
for dist, a, b in heap:
    if find(a) != find(b):
        union(a, b)
        ans += dist


print(f"{ans:.2f}")