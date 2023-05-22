import sys

i=0
while True:
    i+=1
    cnt=0
    l, p, v=map(int, sys.stdin.readline().split())
    if l==0:
        break
    cnt+=(v//p)*l
    if v%p>l:
        cnt+=l
    else:
        cnt+=v%p

    print(f"Case {i}: {cnt}")
    