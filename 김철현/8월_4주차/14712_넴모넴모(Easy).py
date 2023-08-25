import sys
input = sys.stdin.readline 


def solve(r, c):
    global cnt
    if c == m:
        if r == n - 1:
            cnt += 1
            return
        else:
            c = 0
            r += 1
    
    if r == 0 or c == 0:
        arr[r][c] = True
        solve(r, c + 1)
        arr[r][c] = False
        solve(r, c + 1)
    else:
        if 0 <= r - 1 < n and 0 <= c - 1 < m:
            if (not arr[r - 1][c]) or (not arr[r][c - 1]) or (not arr[r - 1][c - 1]):
                arr[r][c] = True
                solve(r, c + 1)
                arr[r][c] = False
            solve(r, c + 1)
    
    return

n, m = map(int, input().split())
arr = [[False] * m for _ in range(n)]

cnt = 0
solve(0, 0)
print(cnt)