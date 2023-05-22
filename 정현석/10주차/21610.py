import sys

# [n, m] = list(map(int, sys.stdin.readline().rstrip().split()))
# board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# movements = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]

n, m = 5, 4
board = [
    [0, 0, 1, 0, 2],
    [2, 3, 2, 1, 0],
    [4, 3, 2, 9, 0],
    [1, 0, 2, 9, 0],
    [8, 8, 2, 1, 0]
]
movements = [
    [1, 3],
    [3, 4],
    [8, 1],
    [4, 8]
]

directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
clouds_board = [[False for _ in range(n)] for _ in range(n)]

for m in movements:                      
    x_dir = directions[m[0]-1][0]
    y_dir = directions[m[0]-1][1]
    dist = m[1]
                    
    for i, c in enumerate(clouds):
        clouds[i] = ((c[0] + x_dir * dist) % n, (c[1] + y_dir * dist) % n)
        
    for c in clouds:
        board[c[0]][c[1]] += 1
        clouds_board[c[0]][c[1]] = True
    
    for c in clouds:
        count = 0
        for d in diag:
            x = c[0] + d[0]
            y = c[1] + d[1]
            if x >= 0 and x < n and y >= 0 and y < n and board[x][y] > 0:
                count += 1
        board[c[0]][c[1]] += count
        
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if not clouds_board[i][j] and board[i][j] >= 2:
                board[i][j] -= 2
                new_clouds.append((i, j))
    
    for c in clouds:
        clouds_board[c[0]][c[1]] = False
    
    clouds = new_clouds
        
print(sum([sum(b) for b in board]))