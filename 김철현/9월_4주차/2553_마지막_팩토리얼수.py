import sys
input = sys.stdin.readline 


N = int(input())
a = 1
cnt = 0
for i in range(1, N + 1):
    temp = i
    while temp % 2 == 0:
        temp //= 2
        cnt += 1
    while temp % 5 == 0:
        temp //= 5
        cnt -= 1
    a = a * temp % 10
    
while cnt:
    a = a * 2 % 10
    cnt -= 1
print(a)