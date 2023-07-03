import sys
from math import ceil                

n, m = map(int, sys.stdin.readline().split())

if m>=7:
    if n>=3:  #모든 방법 사용
        print(m-7+5)
    elif n>=2:     #오른쪽으로 2칸씩
        print(4)
    else:        #이동 불가
        print(1)
else:
    if n>=3:  #오른쪽으로 1칸씩
        print(min(4, m))
    elif n>=2:   #오른쪽으로 2칸씩
        print(ceil(m/2))
    else:
        print(1)
    
