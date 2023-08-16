import sys

n, r, c = map(int, sys.stdin.readline().rstrip().split())


def create_board(start, r, c, n):
    if n == 1:
        return start

    n //= 2

    if r < n and c < n:
        return create_board(start, r, c, n)
    elif r < n and c >= n:
        return create_board(start + n**2, r, c - n, n)
    elif r >= n and c < n:
        return create_board(start + 2 * n**2, r - n, c, n)
    else:
        return create_board(start + 3 * n**2, r - n, c - n, n)


print(create_board(0, r, c, 2**n))
