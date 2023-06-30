import sys
from collections import deque

def check(x, y):
    cnt=0
    for i in range(len(x)):
        if x[i]!=y[i]:
            cnt+=1
        if cnt>=2:
            break
    else:
        if cnt==1:
            return True
    return False
            

n=int(sys.stdin.readline())
s=sys.stdin.readline().strip()

f=deque()
r=deque()
i=0  #앞
j=n-1  #뒤
while i<n and j>=0:
    f.append(s[i])
    r.appendleft(s[j])
    i+=1
    j-=1
    if check("".join(f), "".join(r)):
        print("YES")
        break
else:
    print("NO")