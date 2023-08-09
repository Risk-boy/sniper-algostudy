# import math

# N, A, B, C, D = map(int, input().split())

# # 각 번들만 사용하여 N개 이상의 장미를 구매하는 경우의 최소 비용을 구합니다.
# cost_A_only = B * -(-N // A)
# cost_C_only = D * -(-N // C)

# # 초기 최소 비용을 설정합니다.
# min_cost = min(cost_A_only, cost_C_only)

# # 연립방정식을 통해 x와 y의 근사값을 구합니다.
# x_approx = (D * N) / (A * D + B * C)
# y_approx = -B/D * x_approx + N/D

# # 근사값 주변의 확장된 조합을 검사합니다.
# for dx in range(-100,100):  # -2, -1, 0, 1, 2
#     for dy in range(-100,100):  # -2, -1, 0, 1, 2
#         x = math.floor(x_approx) + dx
#         y = math.floor(y_approx) + dy
#         total_cost = B*x + D*y
#         if A*x + C*y >= N and x>=0 and y>=0:
#             min_cost = min(min_cost, total_cost)

# print(min_cost)

import math

N, A, B, C, D = map(int, input().split())

# 각 번들만 사용하여 N개 이상의 장미를 구매하는 경우의 최소 비용을 구합니다.
cost_A_only = B * -(-N // A)
cost_C_only = D * -(-N // C)

# 초기 최소 비용을 설정합니다.
min_cost = min(cost_A_only, cost_C_only)

# x절편과 y절편 계산
x_intercept = N // A
y_intercept = N // C

# 주변 범위를 탐색하며 최소 비용을 찾습니다.
for dx in range(-1000,1000):
    for dy in range(-1000,1000):
        x = x_intercept + dx
        y = y_intercept + dy
        if x < 0 or y < 0:
            continue
        if A*x + C*y >= N and x>=0 and y>=0:
            total_cost = B*x + D*y
            min_cost = min(min_cost, total_cost)

print(min_cost)