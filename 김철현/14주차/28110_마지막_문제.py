import sys
input = sys.stdin.readline 


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = -1
max_diff = -1
for i in range(n - 1):
    middle = (arr[i] + arr[i + 1]) // 2
    if middle == arr[i]:
        continue
    diff = middle - arr[i]
    if max_diff < diff:
        max_diff = diff
        answer = middle 
        
print(answer)