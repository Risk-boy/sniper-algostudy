import sys 
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

data = defaultdict(set)
for idx in range(N):
    x1,y1,x2,y2 = map(int,input().split())
    data[idx+1].add((x1,y1))
    data[idx+1].add((x2,y2))
    data[0].add((0,0))
print(data)
