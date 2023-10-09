import sys
input = sys.stdin.readline 
from collections import defaultdict


N, M = map(int, input().split())
keyword = [input().rstrip() for _ in range(N)]
dict = defaultdict(bool)
for x in keyword:
    dict[x] = True
cnt = 0
for _ in range(M):
    arr = list(input().rstrip().split(","))
    for x in arr:
        if dict[x]:
            cnt += 1
            dict[x] = False
    
    print(N - cnt)