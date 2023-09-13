import sys


n = int(sys.stdin.readline())
a, b, c, d = [], [], [], []
for _ in range(n):
    q, w, e, r = map(int, sys.stdin.readline().split())
    a.append(q)
    b.append(w)
    c.append(e)
    d.append(r)
    
ab = []
cd = []     
for i in range(n):
    for j in range(n):
        ta = a[i] + b[j]
        tc = c[i] + d[j]
        ab.append(ta)
        cd.append(tc)

ab.sort()
cd.sort()

cnt = 0
l = 0
r = n * n - 1
while l < n * n and r >= 0:
    tmp = ab[l] + cd[r]
    if tmp == 0:
        cntl = 1
        cntr = 1
        while l + 1 < n * n and ab[l + 1] == ab[l]:
            l += 1
            cntl += 1
        while r - 1 >= 0 and cd[r - 1] == cd[r]:
            r -= 1
            cntr += 1
        cnt += cntl * cntr
    if tmp > 0:
        r -= 1
    else:
        l += 1

print(cnt)