import sys

N  = 10 ** 6 + 1
ice = [0 for _ in range(N)]
n, k = map(int, sys.stdin.readline().split())
maxi = -1
answer = 0
for _ in range(n):
    g, i = map(int, sys.stdin.readline().split())
    ice[i] = g
    maxi = max(i, maxi)

r = 2*k + 1
s = answer = sum(ice[:r])

for i in range(r, maxi + 1):
    s += ice[i] - ice[i - r] 
    answer = max(answer, s)
    
print(answer)
    