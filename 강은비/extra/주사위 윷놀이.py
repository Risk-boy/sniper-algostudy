import sys

def dfs(j, score):
    global answer
    if j == 10:
        answer = max(answer, score)
        return
    
    for k in range(4):
        move = dice[j]
        x, y = player[k]
        px, py = x, y
       
        if x == 40 and y >= 1:
            continue

        if y + move < len(board[x]):
            y += move
            move = 0
        else:
            move -= len(board[x]) - 1 - y
            y = len(board[x]) - 1
            
        if move and board[x][y]:
            x = board[x][y]
            y = 0
            if y + move < len(board[x]):
                y += move
                move = 0
            else: 
                move -= len(board[x]) - 1 -y
                y = len(board[x]) - 1
               
        if (x != 25 and board[x][y] % 5 == 0) or (x == 25 and board[x][y] == 40):
            if x < 40:
                x = board[x][y]
                y = 0    
                
            if move:
                y += move
                if x == 40:
                    y = 1
                    
        if not visited[x][y] or (x == 40 and y == 1):
            score += board[x][y]
            player[k] = (x, y)
            visited[x][y] = 1
            visited[px][py] = 0
            dfs(j+1, score)
            score -= board[x][y]
            player[k] = (px, py)
            visited[x][y] = 0
            visited[px][py] = 1
                
dice = list(map(int, sys.stdin.readline().split()))
player = [(0, 0) for _ in range(4)]
board = {0:[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40], 
         10:[10, 13, 16, 19, 25], 
         20:[20, 22, 24, 25], 
         30:[30, 28, 27, 26, 25], 
         25:[25, 30, 35, 40],
         40:[40, 0]}
visited = {k : [0 for _ in board[k]] for k in board}

answer = 0
dfs(0,  0)
print(answer)