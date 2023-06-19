import sys

[n, m] = list(map(int, sys.stdin.readline().rstrip().split()))
hear = {sys.stdin.readline().rstrip() for _ in range(n)}
listen = {sys.stdin.readline().rstrip() for _ in range(m)}

result = sorted(hear & listen)

print(len(result))
for r in result:
    print(r)