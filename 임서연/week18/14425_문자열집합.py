# 문자열

import sys

n, m = map(int, sys.stdin.readline().split())
s = [sys.stdin.readline().rstrip() for _ in range(n)]

cnt = 0
for _ in range(m):
    words = sys.stdin.readline().rstrip()
    if words in s:
        cnt += 1

print(cnt)