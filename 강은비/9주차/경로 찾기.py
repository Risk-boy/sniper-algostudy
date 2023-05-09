import sys

n=int(sys.stdin.readline())
edges=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
            
for k in range(n):
    for x in range(n):
        for y in range(n):
            if edges[x][k] and edges[k][y]:
                edges[x][y]=1
                
for row in edges:
    print(*row)
            
            
            
    