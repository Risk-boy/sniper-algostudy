import sys
input = sys.stdin.readline 


N, M = map(int, input().split())
ls = [0] * M
prefix_sum = [[0] * M for _ in range(N)]
for _ in range(N):
    d, cry = input().rstrip().split()
    if d == "L":
        for i in range(M):
            ls[i] -= int(cry[i])
            prefix_sum[_][i] -= int(cry[i])
    else:
        for i in range(M):
            ls[i] += int(cry[i])
            prefix_sum[_][i] += int(cry[i])

for i in range(M - 1):
    ls[i + 1] += ls[i]

for i in range(N):
    for j in range(M - 1):
        prefix_sum[i][j + 1] += prefix_sum[i][j]

min_v = float("inf")
min_num = -1

for i in range(N):
    max_v = -float("inf")
    for j in range(M):
        temp = abs(ls[j] - prefix_sum[i][j])
        if max_v < temp:
            max_v = temp
    
    if min_v > max_v:
        min_v = max_v
        min_num = i + 1

print(min_num)
print(min_v)