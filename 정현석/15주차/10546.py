import sys

num_participants = int(sys.stdin.readline().rstrip())

participants = set()

while True:
    name = sys.stdin.readline().rstrip()
    if not name:
        break
    else:
        if name not in participants:
            participants.add(name)
        else:
            participants.remove(name)
            
print(*participants)