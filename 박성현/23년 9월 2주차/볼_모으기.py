N = int(input())
balls = input()

# 첫 번째와 마지막에 몇 개의 연속된 빨간색과 파란색 공이 있는지 확인
first_red = first_blue = last_red = last_blue = 0

for ball in balls:
    if ball == 'R':
        first_red += 1
    else:
        break

for ball in balls[::-1]:
    if ball == 'R':
        last_red += 1
    else:
        break

for ball in balls:
    if ball == 'B':
        first_blue += 1
    else:
        break

for ball in balls[::-1]:
    if ball == 'B':
        last_blue += 1
    else:
        break

# 빨간색과 파란색 볼의 총 개수
total_red = balls.count('R')
total_blue = balls.count('B')

# 각 경우에 대해 필요한 이동 횟수 계산
move_r_to_left = total_red - first_red
move_r_to_right = total_red - last_red
move_b_to_left = total_blue - first_blue
move_b_to_right = total_blue - last_blue

# 4가지 경우 중 최소 이동 횟수 출력
print(min(move_r_to_left, move_r_to_right, move_b_to_left, move_b_to_right))