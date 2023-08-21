import sys
from collections import deque

def check():
    for i in range(n):
        y = i
        for x in range(h):
            if board[x][y]:
                y+=board[x][y]
        if y!=i:
            return False
    return True
    
def dfs(cnt):
    global answer
    if check():
        answer = cnt if cnt<answer else answer
        return
    
    if cnt==3 or cnt>=answer:
        return
        
    for j in range(n-1):
        flag = 0
        for i in range(h):
            if flag and board[i][j]==0 and board[i][j+1]==0: 
                continue
            else:
                flag = 0 # 이미 연결된 경우
            if  not flag and board[i][j]==0 and board[i][j+1]==0:
                board[i][j]=1
                board[i][j+1]=-1   
                dfs(cnt+1)   
                board[i][j]=0
                board[i][j+1]=0
                flag = 1   #종료
     
n, m, h = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(n)] for _ in range(h)]
answer=4
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    board[a-1][b-1] = 1
    board[a-1][b] = -1

dfs(0)
if answer<4:
    print(answer)
else:
    print(-1)