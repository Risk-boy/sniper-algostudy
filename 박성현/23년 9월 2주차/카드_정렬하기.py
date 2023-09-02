import heapq
import sys
N = int(input())
data = []
for _ in range(N):
    heapq.heappush(data,int(input()))

result = []
while len(data)>1:
    a = heapq.heappop(data)
    b = heapq.heappop(data)
    c = a+b
    # print(f"c is {c}")
    result.append(c)
    heapq.heappush(data,c)

print(sum(result))
