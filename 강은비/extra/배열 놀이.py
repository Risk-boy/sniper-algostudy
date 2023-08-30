import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    row = [0 for _ in range(n)]
    col = [0 for _ in range(n)]
    for k in range(n):
        s = list(map(int, sys.stdin.readline().split()))
        row[k] = sum(s)
        for i in range(n):
            col[i] += s[i]

    for _ in range(m):
        r1, c1, r2, c2, v = map(int, sys.stdin.readline().split())
        for i in range(r1-1, r2):
            row[i] += (c2-c1+1)*v       
        for i in range(c1-1, c2):
            col[i] += (r2-r1+1)*v
            
    print(*row)
    print(*col)