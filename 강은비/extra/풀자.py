import sys

input = sys.stdin.readline
n, v = map(int, input().split())
arr = list(map(int, input().split()))
answer = n

for i in range(n):
    for j in range(i + 1, n):
        if abs(arr[j] - arr[i]) >= v:
            if i == 0:
                answer = min(answer, 2 + (j - i - 1)// 2)
            else:
                answer = min(answer, 2 + (j - i - 1)// 2 + (i + 1) // 2)
            break
                
print(answer)
