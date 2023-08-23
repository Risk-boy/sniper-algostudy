# 그래프
# DFS, BFS

import sys

n = int(input())
thesis = {}
for _ in range(n):
    x, _, y = sys.stdin.readline().split()
    thesis[x] = y

m = int(input())
for _ in range(m):
    start, _, end = sys.stdin.readline().split()
    if start in thesis.keys():
        middle = thesis[start]
        if middle==end:
            print('T')
        else:
            while middle in thesis.keys():
                middle = thesis[middle]
                if middle==end:
                    print('T')
                    break
            else:
                print('F')
    else:
        print('F')
