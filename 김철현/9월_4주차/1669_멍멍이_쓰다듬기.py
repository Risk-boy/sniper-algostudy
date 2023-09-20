import sys
input = sys.stdin.readline


X, Y = map(int, input().split())

# 0 1 3 6 10 15 21 28

# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 3 4
# 0 1 3 4 5
# 0 1 3 5 6
# 0 1 3 5 6 7
# 0 1 3 5 7 8
# 0 1 3 6 8 9
# 0 1 3 6 8 9 10
# 0 1 3 6 8 10 11
# 0 1 3 6 9 11 12
# 0 1 3 6 9 11 12 13
# 0 1 3 6 9 11 13 14 
# 0 1 3 6 10 12 14 15
# 0 1 3 6 10 13 15 16


diff = Y - X

if diff == 0:
    print(0)
    exit()

n = diff ** 0.5
if n % 1 == 0:
    print(2 * int(n) - 1)
else:
    n = int(n) + 1
    if diff <= (n - 1) * n:
        print(2 * n - 2)
    else:
        print(2 * n - 1)
        