import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
answer = 0
for _ in range(n):
    arr = [0] + list(map(int, input().split()))
    cnt = 0
    one = 0
    two = 0
    for i in range(1, m + 1):
        if arr[i] == 0:
            if one or two:
                cnt += min(one, two) + 1
                one = 0
                two = 0
        if arr[i] == 1 and arr[i - 1] != 1:
            one += 1
        if arr[i] == 2 and arr[i - 1] != 2:
            two += 1
    if one or two:
        cnt += min(one, two) + 1
    answer += cnt

print(answer)
