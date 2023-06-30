import sys
from itertools import combinations

def gcd(x, y):
    if y==0:
        return x
    else:
        return gcd(y, x%y)  #gcd(x, y)==gcd(y, x%y)

def lcm(x, y):
    return (x*y)//gcd(x, y)

nums=list(map(int, sys.stdin.readline().split()))
answers=[]
for c in combinations(nums, 3):
    answers.append(lcm(lcm(c[0], c[1]), c[2]))
answers.sort()
print(answers[0])