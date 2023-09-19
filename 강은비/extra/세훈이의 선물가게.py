import sys
from heapq import heappush, heappop

q = []
a, b, n = map(int, sys.stdin.readline().split())
st = 0
jt = 0
for _ in range(n):
    t, c, m = sys.stdin.readline().split()
    t = int(t)
    m = int(m)
    if c == "B":
        if st < t:
            st = t
        for _ in range(m):
            heappush(q, (st, c))
            st += a
            
    if c == "R":
        if jt < t:
            jt = t
        for _ in range(m):
            heappush(q, (jt, c))    
            jt += b
            
sres = []
jres = []      
i = 0      
while q:
    t, c = heappop(q)
    i += 1
    if c == "B":
        sres.append(i)
    else:
        jres.append(i)
print(len(sres))
print(*sres)
print(len(jres))
print(*jres)
        
    