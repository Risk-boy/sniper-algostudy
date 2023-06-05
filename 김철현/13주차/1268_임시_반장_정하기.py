import sys
input = sys.stdin.readline 


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_cnt = 0
max_number = 0
for i in range(n):
    visited = [False] * n
    visited[i] = True
    for j in range(n):        
        if not visited[j]:
            for k in range(5):
                if arr[i][k] == arr[j][k]:
                    visited[j] = True
                    break
    if sum(visited) > max_cnt:
        max_cnt = sum(visited)
        max_number = i + 1

print(max_number)