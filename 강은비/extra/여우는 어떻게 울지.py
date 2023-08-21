import sys

t = int(sys.stdin.readline())
for _ in range(t):
    l = sys.stdin.readline().split()
    while True:
        s = sys.stdin.readline().split()
        if s[-1]=="say?":
            print(*l)
            break
        else:
            l = [x for x in l if x!=s[-1]]
