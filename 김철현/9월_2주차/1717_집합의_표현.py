import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    
    if x > y:
        parent[x] = y
    elif x < y:
        parent[y] = x
        
        
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a, b)
                    