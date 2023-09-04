import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 1
right = sum(arr) + 1
ans = float("inf")
while left <= right:
    middle = (left + right) // 2
    
    cnt = 0
    temp = 0
    flag = False
    for x in arr:
        if x > middle:
            flag = True
            break
        if temp + x > middle:
            cnt += 1
            temp = x
        else:
            temp += x    
    if temp:
        cnt += 1
        

    if cnt > m or flag:
        left = middle + 1
    else:
        ans = min(ans, middle)
        right = middle - 1

print(ans)