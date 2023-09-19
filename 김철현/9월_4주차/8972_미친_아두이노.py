import sys
input = sys.stdin.readline 


R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
move = list(input().rstrip())

r, c = -1, -1
enemy = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == "R":
            enemy.append((i, j))
        elif arr[i][j] == "I":
            r, c = i, j
            
dr = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

for k in range(len(move)):
    r, c = r + dr[int(move[k])], c + dc[int(move[k])]

    if arr[r][c] == "R":
        print(f"kraj {k + 1}")
        break
    
    visited = [[0] * C for _ in range(R)]

    for i, j in enemy:
        if i < r:
            i += 1
        elif i > r:
            i -= 1
        
        if j < c:
            j += 1
        elif j > c:
            j -= 1

        if i == r and j == c:
            print(f"kraj {k + 1}")
            exit()
        
        visited[i][j] += 1
        
    enemy = []
    for i in range(R):
        for j in range(C):
            if visited[i][j] == 1:
                enemy.append((i, j))

arr = [["."] * C for _ in range(R)]
arr[r][c] = "I"
for i, j in enemy:
    arr[i][j] = "R"

for row in arr:
    print("".join(row))