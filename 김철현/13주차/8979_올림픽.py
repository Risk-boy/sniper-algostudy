import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = []
for _ in range(n):
    number, *medals = map(int, input().split())
    arr.append([number] + medals)

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1
cnt = 0
for i in range(n):
    if i == 0:
        cnt += 1
        if arr[i][0] == k:
            print(rank)
            break
    else:
        if arr[i][1:4] == arr[i - 1][1:4]:
            cnt += 1
        else:
            cnt += 1
            rank = cnt 
        if arr[i][0] == k:
            print(rank)
            break