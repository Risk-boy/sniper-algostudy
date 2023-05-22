import sys

[n, k] = list(map(int, sys.stdin.readline().rstrip().split()))

edges = {}

for i in range(n):
    edges[i] = int(sys.stdin.readline().rstrip())
    
count = 1
node = 0

while count <= n:
    count += 1
    node = edges[node]
    
    if node == k:
        break
    
if count == n + 1:
    print(-1)
else:
    print(count-1)