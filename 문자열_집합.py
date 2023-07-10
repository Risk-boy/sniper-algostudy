import sys 
def input():
    return sys.stdin.readline().rstrip()

A = set()
B = list()

N,M = map(int, input().split())

for i in range(N):
    A.add(input())
for j in range(M):
    B.append(input())

# 처음엔 B도 set으로 설정했었는데 여기에서 에러가 있었음.
count = 0
for b in B:
    if b in A:
        count += 1
print(count)