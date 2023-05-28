import sys
input = sys.stdin.readline 


a = list(input().rstrip())
b = list(input().rstrip())
arr = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
result = []
for i in range(len(a)):
    result.append(arr[ord(a[i]) - 65])
    result.append(arr[ord(b[i]) - 65])

temp = []
while True:
    if len(result) == 2:
        break
    for i in range(len(result) - 1):
        temp.append((result[i] + result[i + 1]) % 10)
    result = temp
    temp = []

for i in range(2):
    print(result[i], end="")