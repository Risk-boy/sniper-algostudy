n, m = map(int, input().split())

# 선견지명으로 알게된 숫자가 주어졌을 경우
if m != 0:
    known_numbers = set(map(int, input().split()))
else:
    known_numbers = set()

# 전체 경우의 수
total_cases = 10**n

# 알지 못하는 숫자만으로 이루어진 경우의 수
unknown_cases = (10 - m)**n

# 선견지명으로 알게된 숫자들만으로 이루어진 경우의 수
only_known_cases = 1
for _ in range(n):
    only_known_cases *= m

result = total_cases - unknown_cases + only_known_cases
print(result)