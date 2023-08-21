import sys

n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
if sum(h)%3 == 0 and sum([x//2 for x in h])>=sum(h)//3:
    print("YES")
else:
    print("NO")
