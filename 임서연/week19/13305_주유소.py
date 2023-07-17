# 그리디
# 시간 - n이 크면 슬라이싱해서 min 찾는 것도 오래 걸림

import sys

n = int(input())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

cheapest = price[0]
pay = 0
for i in range(0, n-1):
    cheapest = min(price[i], cheapest)
    pay += cheapest * road[i]

print(pay)


# cheapest = n
# end = n-1
# pay = 0
# while cheapest!=0:
#     cheapest = price[:cheapest].index(min(price[:cheapest]))
#     pay += price[cheapest] * sum(road[cheapest:end])
#     end = cheapest