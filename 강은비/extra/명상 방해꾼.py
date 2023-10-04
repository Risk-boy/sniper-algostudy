import sys

input = sys.stdin.readline
n, m = map(int, input().split())
bird = []
for _ in range(n):
    d, *x = input().split()
    if d == "L":
        bird.append(list(map(lambda ch: 0 if ch == "0" else -1 , *x)))
    else:
        bird.append(list(map(lambda ch: 0 if ch == "0" else 1 , *x)))
        
summ = [0 for _ in range(m)]        
for i in range(n):
    for j in range(m):
        summ[j] += bird[i][j]

answer = float("inf")
idx = -1
for i in range(n):
    tmp = 0
    mtmp = 0
    for j in range(m):
        tmp += summ[j] - bird[i][j]
        mtmp = max(mtmp, abs(tmp))
    if mtmp < answer:
        idx = i
        answer = mtmp
        
print(idx + 1)
print(answer)