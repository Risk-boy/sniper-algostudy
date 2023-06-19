import sys
input = sys.stdin.readline 
from collections import defaultdict


n = int(input())
dict = defaultdict(list)
for _ in range(n):
    num, pos = map(int, input().split())
    dict[num].append(pos)

cnt = 0
for cow in dict.keys():
    for i in range(len(dict[cow]) - 1):
        if dict[cow][i] != dict[cow][i + 1]:
            cnt += 1

print(cnt)