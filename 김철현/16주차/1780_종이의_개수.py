import sys
input = sys.stdin.readline
from collections import defaultdict


def solve(arr, r, c, m):
    counts = [0, 0, 0]
    for i in range(r, r + m):
        for j in range(c, c + m):
            counts[arr[i][j]] += 1
    if counts.count(0) == 2:
        for i in range(-1, 2):
            if counts[i] != 0:
                dict[i] += 1
        return
    else:
        for i in range(r, r + m, m // 3):
            for j in range(c, c + m, m // 3):
                solve(arr, i, j, m // 3)
    return
        
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dict = defaultdict(int)
solve(arr, 0, 0, n)
for key in range(-1, 2):
    print(dict[key])