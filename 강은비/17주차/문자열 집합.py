import sys

n, m = map(int, sys.stdin.readline().split())
s = set([sys.stdin.readline().rstrip() for _ in range(n)])
t = [sys.stdin.readline().rstrip() for _ in range(m)]

cnt = 0
for x in t:
    if set([x])&s:
        cnt += 1
        
print(cnt)