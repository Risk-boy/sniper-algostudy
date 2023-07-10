import sys

[n, w] = map(int, sys.stdin.readline().rstrip().split())

counter = [0] * (n+1)

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    counter[u] += 1
    counter[v] += 1
    
count = 0
for i in range(2, n+1):
    if counter[i] == 1:
        count += 1
print(w / count)