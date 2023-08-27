def find_decreasing_numbers(n):
    # 기본적으로 0-9까지는 줄어드는 수
    decreasing_numbers = list(range(10))
    idx = 0  # 현재 접근 중인 인덱스
    
    while len(decreasing_numbers) <= n:
        if idx >= len(decreasing_numbers):
            break

        num = decreasing_numbers[idx]
        # 가장 마지막 수
        last_digit = num % 10
        
        # last_digit보다 작은 수로 num을 확장
        for i in range(last_digit):
            new_num = num * 10 + i
            decreasing_numbers.append(new_num)
            
            # 최대값이면 멈춤
            if new_num == 9876543210:
                break

        if 'new_num' in locals() and new_num == 9876543210:
            break
        
        idx += 1  # 다음 숫자로 넘어감.

    if len(decreasing_numbers) < n:
        return -1

    return decreasing_numbers[n-1]

n = int(input())
print(find_decreasing_numbers(n))






