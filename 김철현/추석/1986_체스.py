import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
q, *queen = list(map(int, input().split()))
k, *knight = list(map(int, input().split()))
p, *pawn = list(map(int, input().split()))

arr = [[0] * m for _ in range(n)]
for i in range(0, 2 * p, 2):
    r, c = pawn[i] - 1, pawn[i + 1] - 1
    arr[r][c] = 1

for i in range(0, 2 * k, 2):
    r, c = r, c = knight[i] - 1, knight[i + 1] - 1
    arr[r][c] = 1

for i in range(0, 2 * q, 2):
    r, c = queen[i] - 1, queen[i + 1] - 1
    arr[r][c] = 1
    
qdr = [-1, -1, 0, 1, 1, 1, 0, -1]
qdc = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(0, 2 * q, 2):
    r, c = queen[i] - 1, queen[i + 1] - 1
    for j in range(8):
        nr, nc = r + qdr[j], c + qdc[j]
        while 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 1:
            arr[nr][nc] = 2
            nr += qdr[j]
            nc += qdc[j]
            
kdr = [-2, -1, 1, 2, 2, 1, -1, -2]
kdc = [1, 2, 2, 1, -1, -2, -2, -1]
for i in range(0, 2 * k, 2):
    r, c = knight[i] - 1, knight[i + 1] - 1
    for j in range(8):
        nr, nc = r + kdr[j], c + kdc[j]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 1:
            arr[nr][nc] = 1


ans = 0
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            ans += 1
print(ans)