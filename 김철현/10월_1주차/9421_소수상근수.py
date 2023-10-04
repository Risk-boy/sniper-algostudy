import sys
input = sys.stdin.readline 
from collections import defaultdict


def check(num):
    
    while not dict[num]:
        dict[num] = True
        temp = str(num)
        num = 0
        for x in temp:
            num += int(x) ** 2
        if num == 1:
            return True
    return False

n = int(input())
prime = [True] * (n + 1)
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        j = 2
        while i * j <= n:
            prime[i * j] = False
            j += 1

for i in range(2, n + 1):
    if prime[i]:
        dict = defaultdict(bool)
        if check(i):
            print(i)