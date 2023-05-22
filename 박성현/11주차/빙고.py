import sys
input = sys.stdin.readline

def check_bingo(visited):
    cnt = 0
    for i in range(5):
        if sum([row[i] for row in visited])==5:
            cnt += 1 
        if sum(visited[i])==5:
            cnt += 1
    if sum([visited[i][i] for i in range(5)])==5:
        cnt += 1 
    if sum([visited[i][4-i] for i in range(5)])==5:
        cnt += 1
    return cnt

graph = [list(map(int, input().rstrip().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
call = [list(map(int, input().rstrip().split())) for _ in range(5)]
call_ = []
call_ = []
for i in call:
    for j in i:
        call_.append(j)
        
cnt = 0
X = 0
for call in call_:
    if X >= 3:
        break
    else:            
        for i in range(5):
            for j in range(5):
                if call == graph[i][j]:
                    visited[i][j] = 1
                    X = check_bingo(visited)                    
                    if X >= 3:
                        cnt += 1
                        break
                    else:
                        cnt += 1
print(cnt)