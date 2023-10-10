import sys

def check(stone, check):
    visit = {k : set() for k in stone}          
    for x, y in stone:
        for dx, dy in dir:
            if (dx, dy) not in visit[(x, y)]:
                cnt = 1
                nx = x + dx
                ny = y + dy
                while 0 <= nx < 19 and 0 <= ny < 19:
                    if board[nx][ny] == check and (dx, dy) not in visit[(nx, ny)]:
                        visit[(nx, ny)].add((dx, dy))
                        nx += dx
                        ny += dy
                        cnt += 1
                    else:
                        break
                if cnt == 5:
                    print(check)
                    print(x + 1, y + 1)
                    sys.exit()
    
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(19)]
black = []
white = []
dir = [(0, 1), (1, 0), (-1, 1), (1, 1)]
for j in range(19):
    for i in range(19):
        if board[i][j] == 1:
            black.append((i, j))
            
        if board[i][j] == 2:
            white.append((i, j))
            
check(black, 1)
check(white, 2)

print(0)

