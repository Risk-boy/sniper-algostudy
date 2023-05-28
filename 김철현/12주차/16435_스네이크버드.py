import sys
input = sys.stdin.readline 


n, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
for i in range(n):
    if l >= arr[i]:
        l += 1
    else:
        break

print(l)