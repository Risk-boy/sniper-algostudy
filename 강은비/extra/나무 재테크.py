import sys

n, m, k = map(int, sys.stdin.readline().split())
board = [[5 for _ in range(n)] for _ in range(n)]
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees = [[{} for _ in range(n)] for _ in range(n)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]

for _ in range(m):
    x, y, age = map(int, sys.stdin.readline().split())
    trees[x-1][y-1][age] = 1

for _ in range(k):
    for i in range(n):
        for j in range(n):
            dead = 0
            tmp = {}
            keys = sorted(trees[i][j].keys())
            #spring
            for k in keys:             
                v = trees[i][j].pop(k)
                if board[i][j] >= k*v:
                    board[i][j] -= k*v
                    tmp[k+1] = v
                else:
                    q = board[i][j]//k
                    board[i][j]-=k*q
                    dead+=(k//2)*(v-q)
                    if q:
                        tmp[k+1] = q    
                        
            trees[i][j] = tmp               
            board[i][j] += dead  #summer
            board[i][j] += a[i][j]  #winter
            
    #autumn   
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                if age%5 == 0:
                    for k in range(8):
                        nx, ny = i+d[k][0], j+d[k][1]
                        if 0<=nx<n and 0<=ny<n:
                            trees[nx][ny][1] = trees[nx][ny].get(1, 0)+trees[i][j][age]
                  
answer = 0
for x in trees:
    for t in x:
        answer += sum(t.values())
        
print(answer)