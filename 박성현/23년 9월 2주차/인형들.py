import sys
from decimal import Decimal, getcontext

# decimal의 정밀도 설정
getcontext().prec = 50

def input():
    return sys.stdin.readline().rstrip()

def calc_std(mean, square_sum, n):
    mean = mean / n
    variance = (square_sum / n) - mean ** 2
    if variance < 0:
        variance = Decimal(0)  # 부동소수점 오차로 인한 음수 발생을 방지
    return variance.sqrt()

N, K = map(int, input().split())
data = list(map(int, input().split()))

# 누적합과 누적 제곱합을 저장
pre_sum = [Decimal(0)] * (N + 1)
pre_square_sum = [Decimal(0)] * (N + 1)

for i in range(1, N + 1):
    pre_sum[i] = pre_sum[i-1] + Decimal(data[i-1])
    pre_square_sum[i] = pre_square_sum[i-1] + Decimal(data[i-1] ** 2)

min_std = Decimal('inf')

for i in range(N - K + 1):
    for j in range(i + K, N + 1):
        n = Decimal(j - i)
        mean = pre_sum[j] - pre_sum[i]
        square_sum = pre_square_sum[j] - pre_square_sum[i]
        min_std = min(min_std, calc_std(mean, square_sum, n))

print("{:.11f}".format(min_std))