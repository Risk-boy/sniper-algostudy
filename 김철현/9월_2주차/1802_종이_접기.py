import sys
input = sys.stdin.readline 


def solve(x, n):
    if n == 1:
        return True
    m = n // 2
    left = x[:m]
    right = x[m + 1:]
    for i in range(m):
        if left[i] == right[m - i - 1]:
            return False
    
    if solve(left, m) and solve(right, m):
        return True
    return False

    
T = int(input())
for _ in range(T):
    s = input().rstrip()
    if solve(s, len(s)):
        print("YES")
    else:
        print("NO")