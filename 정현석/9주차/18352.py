import sys
from queue import PriorityQueue

[n, m, k, x] = list(map(int, sys.stdin.readline().rstrip().split()))

edges = {city: [] for city in range(1, n+1)}

for i in range(m):
    [start, end] = list(map(int, sys.stdin.readline().rstrip().split()))
    edges[start].append(end)

dists = {city: float('inf') if city != x else 0 for city in range(1, n+1)}

pq = PriorityQueue()
pq.put((0, x))

while not pq.empty():
        curr_distance, curr_city = pq.get()
        
        if curr_distance > dists[curr_city]:
            continue
        
        for adj in edges[curr_city]:
            dist = curr_distance + 1
            
            if dist < dists[adj]:
                dists[adj] = dist
                pq.put((dist, adj))
    
count = 0
            
for c, v in dists.items():
    if v == k:
        count += 1
        print(c)
        
if count == 0:
    print(-1)