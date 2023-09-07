# 애드 훅
# 분할 정복

import sys

t = int(input())

for _ in range(t):
    fold = list(map(int, sys.stdin.readline().strip()))
    
    n = len(fold)
    a = True
    while n!=1:
        for i in range(n//2):
            if fold[i]==fold[-i-1]:
                a = False
                break
        if a==False:
            print('NO')
            break
        fold = fold[:n//2]
        n = len(fold)

    if a:
        print('YES')
