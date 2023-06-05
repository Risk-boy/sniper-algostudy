import sys
input = sys.stdin.readline 
from collections import defaultdict 


n = int(input())
dict = defaultdict(int)
for _ in range(n):
    a, b = input().split(".")
    dict[b] += 1

for key in sorted(dict.keys()):
    print(key.rstrip(), dict[key])