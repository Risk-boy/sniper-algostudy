import sys
input = sys.stdin.readline 


N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
left = min(arr)
right = left + K

max_v = -1
while left <= right:
    middle = (left + right) // 2
    temp = K
    
    for x in arr:
        if middle > x:
            temp -= (middle - x)
        if temp < 0:
            break
    
    if temp < 0:
        right = middle - 1
    else:
        left = middle + 1
        max_v = max(max_v, middle)

print(max_v)