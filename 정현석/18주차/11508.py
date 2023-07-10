import sys

n = int(sys.stdin.readline().rstrip())
costs = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse = True)

total = 0

for i in range(n):
    if i % 3 != 2:
        total += costs[i]
    
print(total)