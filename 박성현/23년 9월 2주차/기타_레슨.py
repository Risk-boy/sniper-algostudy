import sys
input = sys.stdin.readline

def is_possible(target):
    grpCnt = 1
    total = 0
    for number in numbers:
        total += number
        if total > target:
            grpCnt += 1
            total = number

    return grpCnt <= M

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
left = max(numbers)
right = sum(numbers)

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)