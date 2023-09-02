import sys 
def input():
    return sys.stdin.readline().rstrip()
# 심사대 개수 N, 사람 수 M 입력
N, M = map(int, input().split())

# 각 심사대에서 심사를 마치는 시간 입력
times = [int(input()) for _ in range(N)]

# 이진 탐색을 위한 left와 right 설정
left, right = min(times), max(times) * M

while left <= right:
    mid = (left + right) // 2
    
    # mid 시간동안 심사할 수 있는 총 사람 수 계산
    total_people = sum(mid // time for time in times)
    
    # 모든 사람을 심사할 수 있는 경우
    if total_people >= M:
        answer = mid
        right = mid - 1
    # 모든 사람을 심사할 수 없는 경우
    else:
        left = mid + 1

print(answer)