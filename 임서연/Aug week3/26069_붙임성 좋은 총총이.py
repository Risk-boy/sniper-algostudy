# 자료구조

import sys

n = int(input())

dance = ['ChongChong']
for _ in range(n):
    p1, p2 = sys.stdin.readline().split()
    if p1 in dance or p2 in dance:
        dance += [p1, p2]

print(len(set(dance)))