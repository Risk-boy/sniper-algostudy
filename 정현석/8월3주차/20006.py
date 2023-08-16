import sys

p, m = map(int, sys.stdin.readline().rstrip().split())

rooms = []


def find_room(player):
    if not rooms:
        return -1

    for i, r in enumerate(rooms):
        if r[0] < m and r[1][0][0] - 10 <= player[0] <= r[1][0][0] + 10:
            return i

    return -1


for _ in range(p):
    l, n = sys.stdin.readline().rstrip().split()
    l = int(l)

    i = find_room((l, n))

    if i == -1:
        rooms.append([1, [(l, n)]])
    else:
        rooms[i][0] += 1
        rooms[i][1].append((l, n))

for r in rooms:
    if r[0] < m:
        print("Waiting!")
        for player in sorted(r[1], key=lambda x: x[1]):
            print(*player)
    else:
        print("Started!")
        for player in sorted(r[1], key=lambda x: x[1]):
            print(*player)
