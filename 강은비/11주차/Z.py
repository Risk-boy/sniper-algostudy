import sys

n, r, c=map(int, sys.stdin.readline().split())

res=0
while n>0:
    n-=1
    if r<2**n and c<2**n:  #1사분면 
        pass
    elif r<2**n and c>=2**n: #2사분면 
        res+=(2**n)**2
        c%=2**n
    elif r>=2**n and c<2**n: #3사분면 
        res+=(2**n)**2*2
        r%=2**n
    else:                    #4사분면 
        res+=(2**n)**2*3  
        r%=2**n
        c%=2**n
print(res)
        
        