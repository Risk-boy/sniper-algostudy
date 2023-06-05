import sys

n = int(sys.stdin.readline().rstrip())
serials = [sys.stdin.readline().rstrip() for _ in range(n)]

serials = sorted(serials, key=lambda x: (len(x), sum([int(n) for n in list(x) if n.isnumeric()]), x))

for s in serials:
    print(s)