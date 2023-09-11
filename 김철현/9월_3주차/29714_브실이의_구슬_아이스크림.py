import sys
input = sys.stdin.readline 
from collections import defaultdict


N = int(input())
arr = list(map(int, input().split()))
dict = defaultdict(int)
for x in arr:
    dict[x] += 1
Q = int(input())
for _ in range(Q):
    A = list(map(int, input().split()))[1:]
    dict_A = defaultdict(int)
    
    for a in A:
        dict_A[a] += 1
    check = False
    for a, v in dict_A.items():
        if dict[a] < v:
            check = True
            break
    B = list(map(int, input().split()))[1:]
    dict_B = defaultdict(int)
    for b in B:
        dict_B[b] += 1
    if check:
        continue
    
    for a, v in dict_A.items():
        dict[a] -= v
    for b, v in dict_B.items():
        dict[b] += v

result = []
for x, v in dict.items():
    for i in range(v):
        result.append(x)

length = len(result)
print(length)
if length:
    print(*result)