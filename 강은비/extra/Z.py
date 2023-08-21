import sys

cnt = 0
def find(x, y, n):
    global cnt
    if x==r and y==c:
        print(cnt)
        return
    
    if x<=r<x+n and y<=c<y+n:  #in range -> divide
        find(x, y, n//2)
        find(x, y+n//2, n//2)
        find(x+n//2, y, n//2)
        find(x+n//2, y+n//2, n//2)
        
    else:             #out range  
        cnt+=n**2
    
n, r, c = map(int, sys.stdin.readline().split())
find(0, 0, 2**n)
