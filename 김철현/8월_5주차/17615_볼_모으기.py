import sys
input = sys.stdin.readline 


def right(x, y, cnt):
    check = False
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            if arr[i] == y:
                check = True
        else:
            if arr[i] == x and check:
                cnt += 1
            elif arr[i] == y:
                check = True
    return cnt

def left(x, y, cnt):
    check = False
    for i in range(n):
        if i == 0:
            if arr[i] == y:
                check = True
        else:
            if arr[i] == x and check:
                cnt += 1
            elif arr[i] == y:
                check = True
    return cnt

n = int(input())
arr = list(input().rstrip())
ans = n

ans = min(ans, right("R", "B", 0))
ans = min(ans, left("R", "B", 0))
ans = min(ans, right("B", "R", 0))
ans = min(ans, left("B", "R", 0))

print(ans)