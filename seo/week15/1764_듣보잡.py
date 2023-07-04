import sys

n, m = map(int, sys.stdin.readline().split())

heard = []
for i in range(n):
    heard += [sys.stdin.readline().rstrip()]

see = []
for i in range(m):
    see += [sys.stdin.readline().rstrip()]

heard = set(heard)
see = set(see)

print(len(heard & see))
for x in sorted(heard & see):
    print(x, end="\n")