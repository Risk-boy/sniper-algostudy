import sys
def input():
    return sys.stdin.readline().rstrip() 

N, M, L = map(int, input().split())
rest_stops = list(map(int, input().split()))

# 휴게소 위치를 정렬
rest_stops.sort()

# 이진 탐색 시작
left, right = 1, L
answer = 0

while left <= right:
    mid = (left + right) // 2
    required_stops = 0
    
    last_stop = 0
    for stop in rest_stops:
        # 필요한 휴게소 개수 계산
        required_stops += (stop - last_stop - 1) // mid
        last_stop = stop

    # 마지막 휴게소와 고속도로 끝 사이에 필요한 휴게소 개수
    required_stops += (L - last_stop - 1) // mid

    if required_stops <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
