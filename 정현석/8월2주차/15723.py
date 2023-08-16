import sys

n = int(sys.stdin.readline().rstrip())

p = [sys.stdin.readline().rstrip().split(" is ") for _ in range(n)]

m = int(sys.stdin.readline().rstrip())

pc = [sys.stdin.readline().rstrip().split(" is ") for _ in range(m)]

pd = {}

for a, b in p:
    pd[a] = b


def check(x, y):
    if x == y:
        return "T"

    while x in pd:
        x = pd[x]
        if x == y:
            return "T"
    return "F"


for a, b in pc:
    print(check(a, b))
