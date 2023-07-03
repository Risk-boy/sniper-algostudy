import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(list(sys.stdin.readline().split()))
l.sort(key = lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(l[-1][0])
print(l[0][0])
    