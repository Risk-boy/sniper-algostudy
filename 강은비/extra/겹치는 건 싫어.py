import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = r = 0
m = cnt = 0
num = [0 for _ in range(10 ** 5 + 1)]
while l < n and r < n:
    if num[arr[r]] < k:
        num[arr[r]] += 1
        cnt += 1
    else:
        m = max(cnt, m)
        while l < n and arr[l] != arr[r]:
            num[arr[l]] -= 1
            l += 1
            cnt -= 1
        l += 1
    r += 1
    
print(max(m, cnt))       
