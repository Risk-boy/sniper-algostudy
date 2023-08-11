import sys
input = sys.stdin.readline 
from collections import defaultdict


def dfs(cur, target):
    global check
    if cur == target:
        check = True
        return
    if dict[cur]:
        dfs(dict[cur], target)
    return


n = int(input())
dict = defaultdict(str)
for _ in range(n):
    temp = list(input().split())
    dict[temp[0]] = temp[2]

m = int(input())
for _ in range(m):
    temp = list(input().split())
    check = False
    dfs(temp[0], temp[2])
    if check:
        print("T")
    else:
        print("F")