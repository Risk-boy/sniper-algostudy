import sys
import heapq

n = int(sys.stdin.readline().rstrip())
[r1, c1, r2, c2] = list(map(int, sys.stdin.readline().rstrip().split()))

direction = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

pq = []
heapq.heappush(pq, (0, (r1, c1)))

dist = {(i, j): float('inf') for i in range(n) for j in range(n)}
dist[(r1, c1)] = 0

while pq:
    d, (r, c) = heapq.heappop(pq)
    
    adj = []
    for d in direction:
        r_temp = r + d[0]
        c_temp = c + d[1]
        if r_temp >= 0 and r_temp < n and c_temp >= 0 and c_temp < n:
            adj.append((r_temp, c_temp))
            
    for move in adj:
        if dist[move] > dist[(r, c)] + 1:
            dist[move] = dist[(r, c)] + 1
            heapq.heappush(pq, (dist[move], move))
        
if dist[(r2, c2)] == float('inf'):
    print(-1)
else:
    print(dist[(r2, c2)])