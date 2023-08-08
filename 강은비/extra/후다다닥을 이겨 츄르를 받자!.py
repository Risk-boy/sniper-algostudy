import sys
from collections import defaultdict
import heapq

def find(t, a, b):
    dist[a][b] = 0
    q = []
    heapq.heappush(q, (a, b, 0))
    while q:
        l, n, cd = heapq.heappop(q)
        if dist[l][n]<cd:
            continue
        for d in (-1, 1): #not transfer
            nn = n+d
            if 0<=nn<stations[l] and dist[l][nn]>cd+1:
                dist[l][nn]=cd+1
                heapq.heappush(q, (l, nn, cd+1))
                
        nodes = edges.get(l, {}).get(n, [])  #transfer
        if nodes:
            nl, nn = nodes
            if dist[nl][nn]>cd+t:
                dist[nl][nn]=cd+t
                heapq.heappush(q, (nl, nn, cd+t))
    
n = int(sys.stdin.readline())
stations = list(map(int, sys.stdin.readline().split()))     
m = int(sys.stdin.readline())
edges = defaultdict(dict)
for _ in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    edges[a-1][b-1] = [c-1, d-1]
    edges[c-1][d-1] = [a-1, b-1]
k = int(sys.stdin.readline())
for _ in range(k):
    t, a, b, c, d = map(int, sys.stdin.readline().split())
    dist = [[float('inf') for _ in range(stations[i])] for i in range(n)]
    find(t, a-1, b-1)
    print(dist[c-1][d-1])