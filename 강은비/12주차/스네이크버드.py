import sys

n, h=map(int, sys.stdin.readline().split())
fruit=list(map(int, sys.stdin.readline().split()))
fruit.sort()

for x in fruit:
    if x<=h:
        h+=1
    else:
        break
print(h)