import sys

input = sys.stdin.readline
n = int(input())
m = [[[1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
h = [list(map(int, input().rstrip())) for _ in range(n)]
r = [list(map(int, input().rstrip())) for _ in range(n)]
c = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            m[i][j][k] *= h[j][k]
            m[i][j][k] *= r[i][k]
            m[i][j][k] *= c[i][j]

for i in range(n):
    for j in range(n):
        if h[i][j] == 1:
            cnt = 0
            for k in range(n):
                if m[k][i][j] == 1:
                    cnt += 1
            if not cnt:
                print("NO")
                sys.exit()

for i in range(n):
    for k in range(n):
        if r[i][k] == 1:
            cnt = 0
            for j in range(n):
                if m[i][j][k] == 1:
                    cnt += 1
            if not cnt:
                print("NO")
                sys.exit()
            
for i in range(n):
    for k in range(n):
        if c[i][k] == 1:
            cnt = 0
            for j in range(n):
                if m[i][k][j] == 1:
                    cnt += 1
            if not cnt:
                print("NO")
                sys.exit()

print("YES")        
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(m[i][j][k], end = "")
        print()