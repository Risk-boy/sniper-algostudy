import sys

seq = sys.stdin.readline().rstrip()

prev = seq[0]

count = 1

for c in seq[1:]:
    if c != prev:
        count += 1
        prev = c
        
print(count // 2)