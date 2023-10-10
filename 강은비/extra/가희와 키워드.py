import sys

input = sys.stdin.readline
n, m = map(int, input().split())
keyword = {input().rstrip() : 1 for _ in range(n)}
cnt = n
for _ in range(m):
    for x in input().rstrip().split(","):
        if keyword.get(x, 0):
            keyword.pop(x)
            cnt -= 1
    print(cnt)