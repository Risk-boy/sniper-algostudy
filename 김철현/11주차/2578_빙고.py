import sys
input = sys.stdin.readline 



def check_diagonal():
    check = 0
    cnt = 0
    for i in range(5):
        if visited[i][i]:
            cnt += 1
    if cnt == 5:
        check += 1
    cnt = 0
    for i in range(5):
        if visited[i][4 - i]:
            cnt += 1
    if cnt == 5:
        check += 1
    return check
                

def check_row():
    check = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if visited[i][j]:
                cnt += 1
        if cnt == 5:
            check += 1
    return check


def check_col():
    check = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if visited[j][i]:
                cnt += 1
        if cnt == 5:
            check += 1
    return check


arr = [list(map(int, input().split())) for _ in range(5)]
nums = []
for _ in range(5):
    temp = list(map(int, input().split()))
    for x in temp:
        nums.append(x)

visited = [[False] * 5 for _ in range(5)]
answer = 0
for num in nums:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                visited[i][j] = True
                break
            
    answer += 1
    if check_diagonal() + check_row() + check_col() >= 3:
        print(answer)
        break

