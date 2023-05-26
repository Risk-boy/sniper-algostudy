import sys

num={x:k for x, k in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1])}
A=sys.stdin.readline().strip()
B=sys.stdin.readline().strip()
x=[]

for a, b in zip(A, B):
    x.append(num[a])
    x.append(num[b])

while True:
    tmp=[]
    if len(x)==2:
        print("".join(map(str, x)))
        break    
    for i in range(len(x)-1):
        tmp.append((x[i]+x[i+1])%10)
    x=tmp
            
    