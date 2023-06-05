# 정렬

import sys

n = int(input())
sn = []
for i in range(n):
    guitar = input()
    num_sum = sum([int(x) for x in guitar if x.isdigit()==True])
    sn += [(len(guitar), num_sum, guitar)]

sn.sort()

for ans in sn:
    print(ans[2], end='\n')