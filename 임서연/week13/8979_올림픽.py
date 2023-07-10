# 구현
# 정렬

import sys

n, k = map(int, sys.stdin.readline().split())
total = []
for i in range(n):
    country, gold, silver, bronze = map(int, sys.stdin.readline().split())
    total += [(gold, silver, bronze, country)]

total.sort(reverse=True)

result = []
cnt = 1
sample = total[0][:3]
for j in total:
    if j[:3]!=sample:
        sample = j[:3]
        cnt = len(result)+1
    result += [(j[3], cnt)]

result.sort()
print(result[k-1][1])