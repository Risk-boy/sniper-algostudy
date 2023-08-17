import sys
input = sys.stdin.readline 


def solve(idx, sin, ssn):
    global min_diff
    if idx == n:
        if ssn == 0:
            return
        temp = abs(sin - ssn)
        if temp < min_diff:
            min_diff = temp
        return
    
    solve(idx + 1, sin * arr[idx][0], ssn + arr[idx][1])
    solve(idx + 1, sin, ssn)
    
    return


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_diff = float("inf")

solve(0, 1, 0)
print(min_diff)