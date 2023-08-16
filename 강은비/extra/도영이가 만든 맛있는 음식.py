import sys
from itertools import combinations

n = int(sys.stdin.readline())
s = []
b = []
answer = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    s.append(x)
    b.append(y)

for i in range(1, n+1):
    for c in combinations(range(n), i):
        sour = 1
        bitter = 0 
        for idx in c:
            sour*=s[idx]
            bitter+=b[idx]
        answer.append(abs(sour-bitter))
answer.sort()
print(answer[0])

