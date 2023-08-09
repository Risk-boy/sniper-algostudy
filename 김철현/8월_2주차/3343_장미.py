import sys, math
input = sys.stdin.readline 


n, a, b, c, d = map(int, input().split())

l1 = a / c
l2 = b / d

answer = int(1e18)
if l1 >= l2:
    for i in range(a):
        rest = n - c * i
        temp = 0
        if rest > 0:
            temp = math.ceil(rest / a)
        price = d * i + b * temp
        if answer > price:
            answer = price
        
else:
    for i in range(c):
        rest = n - a * i
        temp = 0
        if rest > 0:
            temp = math.ceil(rest / c)
        price = b * i + d * temp
        if answer > price:
            answer = price
        
print(answer)