import sys

n=int(sys.stdin.readline())
l=[sys.stdin.readline().strip() for _ in range(n)]
l.sort(key=lambda x: (len(x), sum([int(c) for c in x if c.isdigit()]), x))

for x in l:
    print(x)

       

    