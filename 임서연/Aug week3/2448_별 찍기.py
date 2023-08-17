# 재귀

import math

n = int(input())
k = int(math.log2(n/3))
step = [3+2*(2**x-1) if x!=0 else 3 for x in range(k-1)]

star = ['  *  ', ' * * ', '*****']

first = [x for x in star]
second = [x+' '+x for x in star]

def group(i, line):
    if i==len(step):
        return line
    lines = line.copy()
    for idx, x in enumerate(line):
        gap = ' '*6*((step[i]-2)-idx//3)
        lines += [x + gap + ' ' + x]
    i += 1
    return group(i, lines)

if n==3:
    for i in star:
        print(i)
else:
    for idx, i in enumerate(group(0, first+second)):
        q = idx//3
        print(' '*((n-3)-(3*q)), end='')
        print(i, end='')
        print(' '*((n-3)-(3*q)), end='\n')