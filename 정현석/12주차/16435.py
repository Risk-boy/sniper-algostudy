import sys

[n, l] = list(map(int, sys.stdin.readline().rstrip().split()))
fruits = list(map(int, sys.stdin.readline().rstrip().split()))

for f in sorted(fruits):
    if f <= l:
        l += 1
    else:
        break

print(l)