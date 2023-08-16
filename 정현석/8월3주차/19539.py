import sys

n = int(sys.stdin.readline().rstrip())

trees = list(map(int, sys.stdin.readline().rstrip().split()))

total = sum(trees)

q, r = divmod(total, 3)

if r == 0:
    sum_2_q = sum(map(lambda x: x // 2, trees))

    if sum_2_q >= q:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
