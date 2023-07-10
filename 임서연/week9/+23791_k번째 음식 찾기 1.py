# 이분 탐색
# 매개 변수 탐색

# 시간초과

import sys

n = int(input())
korean = list(map(int, sys.stdin.readline().split()))
western = list(map(int, sys.stdin.readline().split()))

q = int(input())

for i in range(q):
    i, j, k = map(int, sys.stdin.readline().split())

    food = [0 for _ in range(i+j)]
    food[0:i] = korean[0:i]
    food[i:] = western[0:j]

    food.sort()
    ans = food[k-1]
    
    if ans in korean:
        print(1, korean.index(ans)+1)
    elif ans in western:
        print(2, western.index(ans)+1)