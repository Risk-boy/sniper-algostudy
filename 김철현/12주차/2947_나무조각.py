import sys
input = sys.stdin.readline 


arr = list(map(int, input().split()))
while True:
    if arr == list(range(1, 6)):
        break
    for i in range(4):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)
