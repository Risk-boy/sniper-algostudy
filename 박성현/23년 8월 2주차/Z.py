import sys
def input():
    return sys.stdin.readline().rstrip()

N, r, c = map(int,input().split())
N_th_list = [(0,0),(0,1),(1,0),(1,1)]
answer = 0
# print(N_th_list.index((1,0)))
if N == 1:
    if (r,c)==(1,1):
        print(0)
    elif (r,c)==(1,2):
        print(1)
    elif (r,c)==(2,1):
        print(2)
    elif (r,c)==(2,2):
        print(3)
else:
    while N>=1:
        r_n = r // 2**(N-1)
        c_n = c // 2**(N-1)
        n = N_th_list.index((r_n, c_n))
        answer += 2**(2*(N-1))*n
        r -= r_n*(2**(N-1))
        c -= c_n*(2**(N-1))
        N -= 1
    print(answer)
    
