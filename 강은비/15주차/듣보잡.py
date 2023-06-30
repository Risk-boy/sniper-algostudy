import sys

n, m=map(int, sys.stdin.readline().split())
d=set(sys.stdin.readline().strip() for _ in range(n))
b=set(sys.stdin.readline().strip() for _ in range(m))
answer=list(d&b)
answer.sort()
print(len(answer))
for x in answer:
    print(x)
