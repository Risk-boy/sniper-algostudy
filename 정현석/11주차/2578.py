import sys

board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]

rows = [0] * 5
cols = [0] * 5
diag = [0] * 2
num_dict = {}

for i in range(5):
    for j in range(5):
        rows[i] += board[i][j]
        cols[j] += board[i][j]
        if i == j:
            diag[0] += board[i][j]
        if i + j == 4:
            diag[1] += board[i][j]
        
        num_dict[board[i][j]] = (i, j)
        
seq = []
for i in range(5):
    seq += list(map(int, sys.stdin.readline().rstrip().split()))
    
count = 0
    
for k in range(len(seq)):
    (i, j) = num_dict[seq[k]]
    rows[i] -= seq[k]
    cols[j] -= seq[k]
    if i == j:
        diag[0] -= board[i][j]
        if diag[0] == 0:
            count += 1
    if i + j == 4:
        diag[1] -= board[i][j]
        if diag[1] == 0:
            count += 1
        
    if rows[i] == 0:
        count += 1
        
    if cols[j] == 0:
        count += 1
        
    if count >= 3:
        break
    
print(k+1)