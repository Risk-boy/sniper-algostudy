import sys

n = int(sys.stdin.readline().rstrip())

meetings = [sys.stdin.readline().rstrip().split() for _ in range(n)]

dancing_people = set()

for p1, p2 in meetings:
    if (
        p1 == "ChongChong"
        or p1 in dancing_people
        or p2 == "ChongChong"
        or p2 in dancing_people
    ):
        dancing_people.add(p1)
        dancing_people.add(p2)

print(len(dancing_people))
