import heapq
import sys 

def input():
    return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(K)]

# 도수가 낮은 순으로 정렬
beers.sort(key=lambda x: x[1])

q = []
total_prefer = 0
min_alcohol = int(2e31) - 1

for prefer, alcohol in beers:
    heapq.heappush(q, prefer)
    total_prefer += prefer
    
    if len(q) > N:
        total_prefer -= heapq.heappop(q)
        
    if len(q) == N and total_prefer >= M:
        min_alcohol = min(min_alcohol, alcohol)
        break

if min_alcohol == int(2e31) - 1:
    print(-1)
else:
    print(min_alcohol)