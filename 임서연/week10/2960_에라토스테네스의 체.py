# 수학
# 구현
# 정수론
# 소수 판정
# 에라토스테네스의 체

import sys

n, k = map(int, sys.stdin.readline().split())

num = (n+1) * [0]
cnt = 0

for i in range(2, n+1):
    if num[i] == 0:
        for j in range(i, n+1, i):
            if num[j] == 0:
                num[j] = 1
                cnt += 1
                if cnt == k:
                    print(j)


# 두번째 if를 넣지 않으면 지웠던 거 또 셈