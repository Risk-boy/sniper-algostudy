def solution(L,P,V):
    answer = 0
    Q = V // P # Q는 몫이다. 
    answer += Q * L
    V = V - (Q * P)
    answer += min(L,V)
    return answer

import sys
# input = sys.stdin.readline
start = 1
while True:
    L, P, V = map(int, input().rstrip().split())
    if L==P==V==0:
        break
    else:
        print("Case {}: {}".format(start, solution(L,P,V)))
        start += 1


        