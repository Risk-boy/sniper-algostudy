import sys

n = int(sys.stdin.readline().rstrip())

edges = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]

for i in range(n):
    while True:
        adjs = [edges[j] for j in range(n) if edges[i][j]]
        
        new_visited = [int(any(j)) for j in zip(*adjs, edges[i])]
        
        if edges[i] == new_visited:
            break
        else:
            edges[i] = new_visited
            
for row in edges:
    print(' '.join([str(i) for i in row]))