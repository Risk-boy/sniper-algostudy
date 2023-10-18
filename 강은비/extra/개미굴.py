import sys

def find(d, i):
    key = sorted(d.keys())
    for k in key:
        print(("--" * i) + k)
        find(d[k], i + 1)
    
cave = {}
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    k, *s = input().split()
    d = cave
    for i in range(int(k)):
        if d.get(s[i], 0) == 0:
            d[s[i]] = {}
        d = d[s[i]]

find(cave, 0)

        
