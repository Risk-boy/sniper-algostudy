import bisect
import sys
def input():
    return sys.stdin.readline().rstrip()

# 입력 받기
N, M = map(int, input().split())
points = list(map(int, input().split()))
segments = [list(map(int, input().split())) for _ in range(M)]

# 점들을 정렬
points.sort()
# 각 선분에 대해 처리
for start, end in segments:
    # 선분의 시작점보다 크거나 같은 첫 번째 점의 인덱스
    start_idx = bisect.bisect_left(points, start)
    # 선분의 끝점보다 큰 첫 번째 점의 인덱스
    end_idx = bisect.bisect_right(points, end)
    # 선분 위에 있는 점의 개수 출력
    print(end_idx - start_idx)