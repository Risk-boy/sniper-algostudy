import sys
import heapq

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

arr = list(map(int, sys.stdin.readline().rstrip().split()))

args = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

for arg in args:
    i, j, k = arg

    print(heapq.nsmallest(k, arr[i-1:j])[-1])