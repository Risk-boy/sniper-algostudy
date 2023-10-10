import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = 10 ** 9 + 7
cnt = 0

p = [1]
for _ in range(n):
    p.append((p[-1] * 2) % m)

for i in range(n - 1, -1, -1):
    if a[i] == k:
        continue
    cnt += p[i]
    cnt %= m
    k = 6 - a[i] - k
    
print(cnt % m)

