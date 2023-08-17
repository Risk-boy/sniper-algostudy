import sys
input = sys.stdin.readline 


def check(start, direction):
    cnt = 1
    max_v = 0
    if direction == 0:
        for i in range(n - 1):
            if arr[start][i] == arr[start][i + 1]:
                cnt += 1
            else:
                if max_v < cnt:
                    max_v = cnt
                cnt = 1
        if max_v < cnt:
                max_v = cnt
    elif direction == 1:
        for i in range(n - 1):
            if arr[i][start] == arr[i + 1][start]:
                cnt += 1
            else:
                if max_v < cnt:
                    max_v = cnt
                cnt = 1
        if max_v < cnt:
                max_v = cnt
    
    return max_v


n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
answer = 0
for i in range(n):
    answer = max(answer, check(i, 0))   # 가로
    answer = max(answer, check(i, 1))   # 세로

for i in range(n):
    for j in range(n - 1):
        if arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            answer = max(answer, check(i, 0))
            answer = max(answer, check(j, 1))
            answer = max(answer, check(j + 1, 1))
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        
        if arr[j][i] != arr[j + 1][i]:
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
            answer = max(answer, check(j, 0))
            answer = max(answer, check(j + 1, 0))
            answer = max(answer, check(i, 1))
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]

print(answer)