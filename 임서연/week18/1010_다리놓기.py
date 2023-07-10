# 수학
# 다이나믹 프로그래밍
# float로는 30! 정도 되는 큰 정수를 정확하게 표현하지 못해 이미 오차가 발생

import sys
import math

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    if n==0 or m==0:
        print(0)
    else:
        bridge = (math.factorial(m) // math.factorial(n)) // int(math.factorial(m-n))
        print(int(bridge))