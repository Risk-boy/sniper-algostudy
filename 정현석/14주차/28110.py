import sys

n = int(sys.stdin.readline().rstrip())
levels = list(map(int, sys.stdin.readline().rstrip().split()))

levels = sorted(levels)
levels_diff = []

max_diff = (levels[1] - levels[0]) // 2
if not max_diff:
    max_index = -1
else:
    max_index = levels[0] + max_diff

for i in range(1, n-1):
    diff = (levels[i+1] - levels[i]) // 2
    
    if not diff:
        continue
    
    if diff > max_diff:
        max_diff = diff
        max_index = levels[i] + max_diff
        
print(max_index)