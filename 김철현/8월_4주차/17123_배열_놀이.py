import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    row = [0] * n
    col = [0] * n
    for i in range(n):
        row[i] = sum(arr[i])
    temp = list(zip(*arr))

    for i in range(n):
        for x in temp[i]:
            col[i] += x
    
    for _ in range(m):
        r1, c1, r2, c2, v = map(int, input().split())
        for i in range(r1 - 1, r2):
            row[i] += ((c2 - c1 + 1) * v)
        for i in range(c1 - 1, c2):
            col[i] += ((r2 - r1 + 1) * v)

    print(*row)
    print(*col)