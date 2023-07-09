# 수학
# 구현

n = int(input())
first = n
cnt = 0

while True:
    a = n//10
    b = n%10
    n = a + b

    n = 10*b + n%10
    cnt += 1

    if n == first:
        break

print(cnt)
