import sys
from math import ceil


n, an, ap, bn, bp = map(int, sys.stdin.readline().rstrip().split())

if ap * bn < bp * an:
    an, ap, bn, bp = bn, bp, an, ap


min_price = float("inf")

for ac in range(bn):
    bc = ceil((n - ac * an) / bn)

    if bc < 0:
        min_price = min(min_price, ac * ap)
        break

    min_price = min(min_price, ac * ap + bc * bp)

print(min_price)
