# 완전탐색
# 브루트포스 알고리즘

import sys
a, b, c, d, e = map(int, sys.stdin.readline().split())

number = [a, b, c, d, e]

combination = [(0,1,2), (0,1,3), (0,1,4), (0,2,3), (0,2,4), 
               (0,3,4), (1,2,3), (1,2,4), (1,3,4), (2,3,4)]

common = []
for comb in combination:    
    i, j, k = number[comb[0]], number[comb[1]], number[comb[2]]
    
    max_num = i*j*k
    
    first = [x for x in range(1, max_num+1) if x%i==0]
    second = [x for x in first if x%j==0]
    final = [x for x in second if x%k==0]

    common += final

common.sort()
print(common[0])