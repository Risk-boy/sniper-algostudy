import sys
input = sys.stdin.readline 
from collections import defaultdict
from heapq import heappush, heappop

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
A = defaultdict(int)
q1 = []
q2 = []
for i in range(1, N + 1):
    A[i] = arr[i - 1]
    heappush(q1, (arr[i - 1], i))
for i in range(1, M + 1):
    A[i + N] = arr2[i - 1]
    heappush(q2, (arr2[i - 1], i + N))
    
K = int(input())
for _ in range(K):
    temp = list(input().rstrip().split())
    if temp[0] == "U":
        x, y = int(temp[1]), int(temp[2])
        A[x] = y
        if x <= N:
            heappush(q1, (y, x))
        else:
            heappush(q2, (y, x))
    else:
        a = b = 0
        while True:
            dist, num = heappop(q1)
            if A[num] == dist:
                a = num
                heappush(q1, (dist, num))
                break
        
        while True:
            dist, num = heappop(q2)
            if A[num] == dist:
                b = num
                heappush(q2, (dist, num))
                break
                    
        print(a, b)