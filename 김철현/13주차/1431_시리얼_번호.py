import sys
input = sys.stdin.readline 


n = int(input())
arr = []
for _ in range(n):
    serial = input().rstrip()
    sum = 0
    for x in serial:
        if x in "123456789":
            sum += int(x)
    arr.append([len(serial), sum, serial])

arr.sort(key=lambda x:(x[0], x[1], x[2]))
for i in range(n):
    print(arr[i][2])