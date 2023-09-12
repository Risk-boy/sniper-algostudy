S = int(input())

left = 1
right = int(4294967295)  # 임의로 큰 수로 설정
answer = 0

while left <= right:
    mid = (left + right) // 2
    if mid * (mid + 1) // 2 <= S:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)