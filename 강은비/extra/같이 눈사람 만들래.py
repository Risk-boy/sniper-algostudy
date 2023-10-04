import sys

input = sys.stdin.readline
n = int(input())
h = list(map(int, input().split()))
comb = []
for i in range(n):
    for j in range(i + 1, n):
        comb.append((h[i] + h[j], i, j))
comb.sort()

answer = float("inf")
for i in range(len(comb) - 1):
    a = comb[i]
    b = comb[i + 1]
    if a[1] != b[1] and a[1] != b[2] and a[2] != b[1] and a[2] != b[2]:
        answer = min(answer, abs(a[0] - b[0]))
        if answer == 0:
            print(answer)
            break
else:
    print(answer)
        