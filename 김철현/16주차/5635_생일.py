import sys
input = sys.stdin.readline 


n = int(input())
arr = []
for _ in range(n):
    name, d, m, y = input().rstrip().split()
    arr.append([int(y), int(m), int(d), name])

arr.sort(key=lambda x: (x[0], x[1], x[2]))
print(arr[-1][3])
print(arr[0][3])