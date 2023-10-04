import sys
input = sys.stdin.readline 


def check(r, c, color):
    
    for k in range(4):
        cnt = 1
        nr, nc = r + dr[k], c + dc[k]
        
        while 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == color:
            cnt += 1
            
            if cnt == 5:
                if 0 <= nr + dr[k] < n and 0 <= nc + dc[k] < n and arr[nr + dr[k]][nc + dc[k]] == color:
                    break
                if 0 <= r - dr[k] < n and 0 <= c - dc[k] < n and arr[r - dr[k]][c - dc[k]] == color:
                    break
                
                print(color)
                print(r + 1, c + 1)
                exit()

            nr += dr[k]
            nc += dc[k]
    return


n = 19
arr = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            check(i, j, arr[i][j])

print(0)