import sys

[n, m] = map(int, sys.stdin.readline().rstrip().split())

strings = set()

for _ in range(n):
    strings.add(sys.stdin.readline().rstrip())

count = 0

for _ in range(m):
    if sys.stdin.readline().rstrip() in strings:
        count += 1
        
print(count)