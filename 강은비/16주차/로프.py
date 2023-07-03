import sys

n = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(n)]

rope.sort(reverse=True)
m = rope[0]

for i in range(1, n):
    t = rope[i]*(i+1)
    if t > m:
        m = t
print(m)