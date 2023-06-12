import sys

[n, m, k] = list(map(int, sys.stdin.readline().rstrip().split()))

v = [0] * n

for _ in range(m):
    v[int(sys.stdin.readline().rstrip())] = 1

l = 0
while k:
    l += 1
    if k % 2:
        w = v.copy()
        for i in range(n):
            v[i] ^= w[(i + 2 ** l) % n]
    k //= 2
    
print(sum(v))