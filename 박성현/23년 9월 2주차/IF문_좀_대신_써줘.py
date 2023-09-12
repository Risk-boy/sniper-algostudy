import bisect
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
titles = {}
powers = []

# 칭호와 전투력 상한값을 입력 받는다.
for _ in range(N):
    title, power = input().split()
    power = int(power)
    
    # 같은 전투력 상한값이 여러 번 나오더라도 첫 번째로 나온 칭호만 저장한다.
    if power not in titles:
        titles[power] = title
        powers.append(power)

result_list = []

# 캐릭터의 전투력에 따른 칭호를 찾는다.
for _ in range(M):
    power = int(input())
    idx = bisect.bisect_left(powers, power)
    result_list.append(titles[powers[idx]])

print('\n'.join(result_list))