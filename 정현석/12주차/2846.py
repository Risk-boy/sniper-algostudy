import sys

n = int(sys.stdin.readline().rstrip())

p = list(map(int, sys.stdin.readline().rstrip().split()))

prev = p[0]
start = p[0]

max_len = 0

for num in p[1:]:
    if prev >= num:
        start = num
    else:
        max_len = max(max_len, num - start)
    
    prev = num
        
print(max_len)