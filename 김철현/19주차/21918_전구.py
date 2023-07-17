import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b] = c
    elif a == 2:
        for i in range(b, c + 1):
            arr[i] = (arr[i] + 1) % 2
    elif a == 3:
        for i in range(b, c + 1):
            arr[i] = 0
    else:
        for i in range(b, c + 1):
            arr[i] = 1

print(*arr[1:])