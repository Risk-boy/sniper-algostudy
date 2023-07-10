import sys
import math
def input():
    return sys.stdin.readline().rstrip()

test_case = int(input())
for _ in range(test_case):
    a, b = map(int, input().split())
    print(math.comb(b,a))
