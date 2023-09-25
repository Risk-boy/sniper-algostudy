import sys
input = sys.stdin.readline 


N = int(input())
A = []
for _ in range(N):
    _, *time = list(map(int, input().split()))
    A.append(sum(time))

A.sort()
for i in range(1, N):
    A[i] += A[i - 1]

print(sum(A))