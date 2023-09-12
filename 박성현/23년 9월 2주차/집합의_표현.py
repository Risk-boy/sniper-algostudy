import sys
def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
parents = [i for i in range(N+1)]

def find_parent(parents, x):
    if parents[x]!=x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_find(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a!=b:
        parents[b]=a

for _ in range(M):
    case, a, b = map(int,input().split())
    if case == 0:
        union_find(parents,a,b)
    else:
        if find_parent(parents, a)==find_parent(parents, b):
            print('YES')
        else:
            print('NO')