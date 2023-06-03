import sys

n=int(sys.stdin.readline())
n*=2
x=int(n**0.5)
if x*(x+1)>n:
    print(x-1)
else:
    print(x)
