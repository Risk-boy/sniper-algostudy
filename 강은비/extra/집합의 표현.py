import sys

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y, check = False):
    x = find(x)
    y = find(y)

    if x == y:
        return "YES"

    if x != y:
        if check:
            return "NO"
        parent[y] = x
        
n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
for _ in range(m):
    x, a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    if x == "0":
        union(a, b)
    else:
        print(union(a, b, check=True))