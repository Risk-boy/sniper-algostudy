import sys

n = int(sys.stdin.readline())
prices = [int(sys.stdin.readline()) for _ in range(n)]

prices.sort(reverse=True)
p = 0
for i in range(1, n+1):
    if i%3 == 0:
        continue
    else:
        p+=prices[i-1]
print(p)