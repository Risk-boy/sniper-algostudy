'''
1. 명검을 써서 가는 경우와, 그렇지 않은 경우의 최소 거리를 각각 갱신해줘야한다.
2. dfs로 풀 수 있을 것 같은데
3. 명검을 얻었는지 여부를 체크하는 함수가 있어야할 것 같다. visited는 따로 저장해줘야할 것 같다.
'''

import sys 
def input():
    return sys.stdin.readline().rstrip()

from collections import deque

N, M, T = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]

# BFS를 위한 초기 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[False]*M for _ in range(N)] for _ in range(2)]  # 그람을 가진 상태 / 안 가진 상태
q = deque([(0, 0, 0, 0)])  # x, y, time, 그람을 가졌는지 여부

# 최단 시간을 저장할 변수
shortest_time = float('inf')  # 'inf'는 무한대를 의미

# BFS
while q:
    x, y, time, got_sword = q.popleft()

    # 시간이 T를 넘으면 실패
    if time > T:
        continue  # 다른 경우를 계속 확인

    # 공주를 구출했다면
    if x == N-1 and y == M-1:
        shortest_time = min(shortest_time, time)  # 최단 시간 갱신

    # 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 경계 체크
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 이미 방문한 곳이면 skip
        if visited[got_sword][nx][ny]:
            continue

        # 그람을 얻었거나, 그람을 얻지 않았지만 벽이 없는 경우
        if castle[nx][ny] != 1 or got_sword:
            visited[got_sword][nx][ny] = True
            q.append((nx, ny, time + 1, got_sword))

        # 그람을 얻는 경우
        if castle[nx][ny] == 2:
            visited[1][nx][ny] = True
            q.append((nx, ny, time + 1, 1))

# 결과 출력
if shortest_time <= T:
    print(shortest_time)
else:
    print("Fail")