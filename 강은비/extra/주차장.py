import sys
from heapq import heappush, heappop

def save():
    global total
    
    k = heappop(park)
    total += Rs[k] * car[i - 1][0]
    car[i - 1].append(k)
    

input = sys.stdin.readline
n, m = map(int, input().split())
Rs = [int(input()) for _ in range(n)]
car = [[int(input())] for _ in range(m)]
wait = []
park = []

for i in range(n):
    heappush(park, i)

total = 0
for _ in range(2 * m):
    i = int(input())
    if i > 0:
        if park:
            save()
        else:
            wait.append(i)
    else:
        heappush(park, car[-i - 1][1])
        while wait and park:
            i = wait.pop(0)
            save()
        
print(total)