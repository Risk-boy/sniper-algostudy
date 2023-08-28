import sys
input = sys.stdin.readline 


n = int(input())
arr = list(map(int, input().split()))
min_diff = 2 * int(1e9)
start = 0
end = n - 1
while start < end:
    diff = arr[end] + arr[start]
    
    if abs(min_diff) > abs(diff):
        min_diff = diff

    if diff == 0:
        break
    elif diff < 0:
        start += 1
    else:
        end -= 1

print(min_diff)