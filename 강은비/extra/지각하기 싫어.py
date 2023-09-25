import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n, m = map(int, input().split())
fq = []
bq = []
f = [0 for _ in range(n)]
b = [0 for _ in range(m)]
for i, x in enumerate(map(int, input().split())):
    heappush(fq, (x, i + 1))
    f[i] = x
for i, x in enumerate(map(int, input().split())):
    heappush(bq, (x, n + i + 1))
    b[i] = x
    
for _ in range(int(input())):
    o, *idx = input().split()
    if o == "L":
        while fq[0][0] != f[fq[0][1] - 1]:
            heappop(fq)
        while bq[0][0] != b[bq[0][1] - 1 - n]:
            heappop(bq)
        print(fq[0][1], bq[0][1])
    else:
        i, y = map(int, idx)
        if i <= n:
            heappush(fq, (y, i))
            f[i - 1] = y
        else:
            heappush(bq, (y, i))
            b[i - 1 - n] = y
    
