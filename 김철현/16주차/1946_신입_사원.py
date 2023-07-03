import sys
input = sys.stdin.readline 


T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append((list(map(int, input().split()))))
    arr.sort(key=lambda x: x[0])

    max_cnt = 0
    threshold = n + 1
    for i in range(n):
        if arr[i][1] < threshold:
            max_cnt += 1
            threshold = arr[i][1]
    print(max_cnt)