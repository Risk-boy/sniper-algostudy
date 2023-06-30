import sys

n = int(sys.stdin.readline().rstrip())

ropes = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])

max_weight = 0

for r in ropes:
    curr_weight = n * r
    
    if curr_weight > max_weight:
        max_weight = curr_weight

    n -= 1

print(max_weight)