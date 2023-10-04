import sys

n = int(sys.stdin.readline())
prime = [0 for i in range(n + 1)]
for i in range(2, n + 1):
    if prime[i] == 1:
        continue
    for j in range(2 * i, n + 1, i):
        prime[j] = 1
        
num = []
for i in range(2, n + 1):
    if prime[i] == 0:
        num.append(i)

for x in num:
    tmp = x
    visit = [0 for _ in range(487)]
    while True:
        s = 0
        while tmp:
            s += (tmp % 10) ** 2
            tmp //= 10
            
        if s == 1:
            print(x)
            break
        
        if visit[s]:
            break
        
        visit[s] = 1
        tmp = s