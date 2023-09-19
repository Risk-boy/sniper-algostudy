import sys
input = sys.stdin.readline 


def solve(n):
    if n == 1:
        print("Possible")
        exit()
    
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if arr[r][c] == 2:
                for k in range(8):
                    nr, nc = r + dr[k], c + dc[k]
                    nnr, nnc = nr + dr[k], nc + dc[k]
                    if 1 <= nr < N - 1 and 1 <= nc < N - 1 and 1 <= nnr < N - 1 and 1 <= nnc < N - 1:
                        if arr[nnr][nnc] == 0 and arr[nr][nc] == 2:
                            arr[r][c] = 0
                            arr[nr][nc] = 0
                            arr[nnr][nnc] = 2
                            solve(n - 1)
                            arr[r][c] = 2
                            arr[nr][nc] = 2
                            arr[nnr][nnc] = 0
    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            cnt += 1

if cnt == 0:
    print("Impossible")
    exit()
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

solve(cnt)
print("Impossible")