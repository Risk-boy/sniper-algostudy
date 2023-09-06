import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
answer = float("inf")

for i in range(n):
    s = e = 0
    for j in range(i, n):
        s += num[j]
        e += num[j]**2
        cnt = j-i+1
        if cnt >= k:
           answer = min(answer, (e/cnt - (s/cnt)**2)**0.5)
        
print(answer)