import sys

p, m = map(int, sys.stdin.readline().split())
rooms = []
for _ in range(p):
    l, n = sys.stdin.readline().split()
    if not rooms:
        rooms.append([(l, n)])
        continue
    for r in rooms:
        k = int(r[0][0])
        if len(r)<m and k-10<=int(l)<=k+10:
            r.append((l, n))
            break
    else:
        rooms.append([(l, n)])
for r in rooms:
    if len(r)==m:
        print("Started!")
    else:
        print("Waiting!")
    r.sort(key = lambda x: x[1])
    for x in r:
        print(*x)  