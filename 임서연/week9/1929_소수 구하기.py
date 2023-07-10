# 수학
# 정수론
# 소수 판정
# 에라토스테네스의 체

import sys
m, n = map(int, sys.stdin.readline().split())

# for num in range(m, n+1):
#     prime = []
#     for x in range(1, num//2+1):
#         if num%x == 0:
#             prime.append(x)
#         else:
#             pass
    
#     if len(prime)==1:
#         print(num)

num = (n+1) * [0]

for i in range(2, n+1):
    if num[i] == 0:
        if i >= m:
            print(i)
        for j in range(i, n+1, i):
            num[j] = 1


# 'range' 빼먹지 말기
# range 확인