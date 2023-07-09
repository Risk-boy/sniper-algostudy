# 브루트포스 알고리즘

import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

card.sort(reverse=True)

sum_list = []
sum = 0
for i in range(0, n-2):
    if card[i] < m:
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                sum = card[i] + card[j] + card[k]
                if sum <= m:
                    sum_list += [sum]

print(max(sum_list))