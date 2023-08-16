import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    sound = sys.stdin.readline().rstrip().split()
    sound_set = set(sound)

    while True:
        animal_sound = sys.stdin.readline().rstrip().split()

        if animal_sound[0] != "what":
            sound_set.discard(animal_sound[2])
        else:
            print(*filter(lambda s: s in sound_set, sound))
            break
