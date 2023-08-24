import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
left = max(arr)
right = 10000 * n

while left <= right:
    middle = (left + right) // 2
    
    cnt = 0
    temp = 0
    for x in arr:
        if temp < x:
            cnt += 1
            temp = middle    
        temp -= x
            
    if cnt > m:
        left = middle + 1
    else:
        right = middle - 1

print(left)