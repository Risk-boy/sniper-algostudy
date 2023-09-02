import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
l = 0
r = n-1
answer = float("inf")
while l<r:
    k = a[l]+a[r]
    if k>0:
        r-=1
    elif k<0:
        l+=1
    else:
        print(k)
        break
    if abs(k)<abs(answer):
        answer = k
else:
    print(answer)    
