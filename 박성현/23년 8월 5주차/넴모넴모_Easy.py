import sys

N, M = map(int, sys.stdin.readline().split())
bbuyo = [[0]*(M+1) for _ in range(N+1)]
answer = 0

def dfs(cnt):
    global answer
    if cnt == N * M:
        answer += 1
        return
    
    y = cnt // M + 1
    x = cnt  % M + 1
    
    dfs(cnt + 1)
    if bbuyo[y - 1][x] == 0 or bbuyo[y][x - 1] == 0 or bbuyo[y - 1][x - 1] == 0: 
        bbuyo[y][x] = 1
        dfs(cnt + 1)
        bbuyo[y][x] = 0
        
        
dfs(0)
print(answer)