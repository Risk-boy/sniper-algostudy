import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = float("inf")
for i in range(n):
    a = b = 0
    for j in range(i, n):
        a += arr[j]
        b += arr[j] ** 2
        num = j - i + 1
        if num >= k:
            answer = min(answer, ((b * num - a ** 2) / num ** 2) ** 0.5)

print(answer)