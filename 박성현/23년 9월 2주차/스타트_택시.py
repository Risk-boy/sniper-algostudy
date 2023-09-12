from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, board):
    n = len(board)
    dist = [[-1] * n for _ in range(n)]
    dist[x][y] = 0
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist

def find_passenger(taxi, passengers, board):
    distances = bfs(taxi[0], taxi[1], board)
    min_distance = float('inf')
    target = None
    for passenger in passengers:
        sx, sy, _, _ = passenger
        if distances[sx][sy] != -1 and distances[sx][sy] < min_distance:
            min_distance = distances[sx][sy]
            target = passenger
        elif distances[sx][sy] != -1 and distances[sx][sy] == min_distance:
            if sx < target[0] or (sx == target[0] and sy < target[1]):
                target = passenger
    return target, min_distance

def solution(n, m, fuel, board, taxi, passengers):
    for _ in range(m):
        passenger, pickup_dist = find_passenger(taxi, passengers, board)
        if not passenger or fuel < pickup_dist:
            return -1
        fuel -= pickup_dist
        taxi = (passenger[0], passenger[1])

        dropoff_dist = bfs(taxi[0], taxi[1], board)[passenger[2]][passenger[3]]
        if dropoff_dist == -1 or fuel < dropoff_dist:
            return -1
        fuel += dropoff_dist
        taxi = (passenger[2], passenger[3])

        passengers.remove(passenger)
    return fuel

n, m, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
tx, ty = map(int, input().split())
taxi = (tx-1, ty-1)
passengers = [tuple(map(int, input().split())) for _ in range(m)]
for i in range(m):
    sx, sy, ex, ey = passengers[i]
    passengers[i] = (sx-1, sy-1, ex-1, ey-1)

print(solution(n, m, fuel, board, taxi, passengers))