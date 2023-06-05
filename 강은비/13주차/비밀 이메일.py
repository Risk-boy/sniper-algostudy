import sys

def getr(n):
    for i in range(int(n**0.5), 0, -1):
        if n%i==0:
            return i
s=sys.stdin.readline().strip()
n=len(s)
r=getr(n)
c=n//r
for i in range(0, r):
    for j in range(i, n, r):
        print(s[j], end="")


