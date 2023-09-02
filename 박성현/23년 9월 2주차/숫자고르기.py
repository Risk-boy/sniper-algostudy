N = int(input())
arr = [0]  # 1-based indexing을 위한 더미 값
for _ in range(N):
    arr.append(int(input()))

visited = [False] * (N + 1)  # 방문 여부 체크 배열
finished = [False] * (N + 1)  # DFS가 종료된 노드인지 체크하는 배열
result = []  # 답을 저장할 배열

def dfs(start):
    global result
    visited[start] = True
    next_num = arr[start]
    
    if not visited[next_num]:
        dfs(next_num)
    elif not finished[next_num]:
        # 루프 찾기
        temp = []
        while next_num != start:
            temp.append(next_num)
            next_num = arr[next_num]
        temp.append(next_num)
        result += temp
    
    finished[start] = True

# 각 노드마다 DFS 수행
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

result.sort()
print(len(result))
for num in result:
    print(num)