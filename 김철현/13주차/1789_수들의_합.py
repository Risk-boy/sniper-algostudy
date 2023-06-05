import sys
input = sys.stdin.readline 


s = int(input())

sum = 0
for i in range(1, s + 1):
    sum += i
    if sum > s:
        print(i - 1)
        break
    elif sum == s:
        print(i)
        break
    