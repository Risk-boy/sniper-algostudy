import sys
input = sys.stdin.readline 


n = int(input())
arr = [0] + list(map(int, input().split()))
pre_check = [0] * (n + 1)
for i in range(1, n):
    if arr[i] > arr[i + 1]:
        pre_check[i + 1] = 1
    pre_check[i + 1] += pre_check[i]

q = int(input())
for _ in range(q):
    start, end = map(int, input().split())
    print(pre_check[end] - pre_check[start])