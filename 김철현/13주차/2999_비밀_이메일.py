import sys
input = sys.stdin.readline 


word = list(input().rstrip())
n = len(word)
r = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        r = i

c = n // r
arr = [[""] * c for _ in range(r)]
idx = 0
for i in range(c):
    for j in range(r):
        arr[j][i] = word[idx]
        idx += 1

for i in range(r):
    for j in range(c):
        print(arr[i][j], end="")