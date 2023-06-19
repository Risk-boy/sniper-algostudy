import sys
input = sys.stdin.readline 
from collections import defaultdict


n = int(input())
dict = defaultdict(int)
for _ in range(n):
    dict[input().rstrip()] += 1

for _ in range(n - 1):
    dict[input().rstrip()] -= 1

for name in dict.keys():
    if dict[name] == 1:
        print(name)