import sys
input = sys.stdin.readline 


n = int(input())
H = [list(map(int, input().rstrip())) for _ in range(n)]
R = [list(map(int, input().rstrip())) for _ in range(n)]
C = [list(map(int, input().rstrip())) for _ in range(n)]

M = [[[1] * n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if H[j][k] == 0:
                M[i][j][k] = 0
            
            if R[i][k] == 0:
                M[i][j][k] = 0
            
            if C[i][j] == 0:
                M[i][j][k] = 0
            
for j in range(n):
    for k in range(n):
        if H[j][k] == 1:
            for i in range(n):
                if M[i][j][k] == 1:
                    break
            else:
                print("NO")
                exit()

for i in range(n):
    for k in range(n):
        if R[i][k] == 1:
            for j in range(n):
                if M[i][j][k] == 1:
                    break
            else:
                print("NO")
                exit()

for i in range(n):
    for j in range(n):
        if C[i][j] == 1:
            for k in range(n):
                if M[i][j][k] == 1:
                    break
            else:
                print("NO")
                exit()

            
            
print("YES")
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(M[i][j][k], end="")
        print()