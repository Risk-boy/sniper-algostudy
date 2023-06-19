import sys

[r, c] = list(map(int, sys.stdin.readline().rstrip().split()))

board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
new_board = [b.copy() for b in board]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

lands_r = []
lands_c = []

for i in range(r):
    for j in range(c):
        if board[i][j] == 'X':
            num_sea = 0
            for d in directions:
                adj_r = i+d[0]
                adj_c = j+d[1]
                if adj_r < 0 or adj_c < 0 or adj_r >= r or adj_c >= c or board[adj_r][adj_c] == '.':
                    num_sea += 1
            
            if num_sea >= 3:
                new_board[i][j] = '.'
            else:
                lands_r.append(i)
                lands_c.append(j)
               
[min_r, max_r, min_c, max_c] = [min(lands_r), max(lands_r), min(lands_c), max(lands_c)]

for i in range(min_r, max_r+1):
    print(''.join(new_board[i][min_c: max_c+1]))