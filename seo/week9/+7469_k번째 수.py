# 자료 구조
# 정렬
# 세그먼트 트리
# 이분 탐색
# 머지 소트 트리

# 시간초과

import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for x in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    need = arr[i-1:j]
    need.sort()
    print(need[k-1])