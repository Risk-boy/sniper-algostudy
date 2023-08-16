import sys

n = int(sys.stdin.readline().rstrip())
graph = ["  *  ", " * * ", "*****"]
bottom = 5

while n > 3:
    additional = " " * ((bottom >> 1) + 1)

    graph = [additional + row + additional for row in graph] + [
        row + " " + row for row in graph
    ]
    bottom = (bottom << 1) + 1

    n >>= 1

for row in graph:
    print(row)
