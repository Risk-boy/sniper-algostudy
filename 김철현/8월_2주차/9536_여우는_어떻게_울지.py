import sys
input = sys.stdin.readline 


T = int(input())
for _ in range(T):
    arr = list(input().split())
    others = set()
    while True:
        temp = list(input().split())
        if temp[-1] == "say?":
            break
        others.add(temp[2])
    for x in arr:
        if x not in others:
            print(x, end=" ")