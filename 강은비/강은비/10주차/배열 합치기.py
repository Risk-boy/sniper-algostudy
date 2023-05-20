import sys
import heapq

n, m=map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
b=list(map(int, sys.stdin.readline().split()))

heapq.heapify(a)
heapq.heapify(b)

while a or b:
    if a and b:
        if a[0]<b[0]:
            print(heapq.heappop(a), end=" ")
        else:
            print(heapq.heappop(b), end=" ")
    elif a:
        print(heapq.heappop(a), end=" ")
    else:
        print(heapq.heappop(b), end=" ")