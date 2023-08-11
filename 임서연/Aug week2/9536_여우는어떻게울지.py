# 문자열
# 파싱

import sys

t = int(input())

for _ in range(t):
    noise = sys.stdin.readline().split()

    sound_list = []
    while True:
        animal, *_, sound = sys.stdin.readline().split()
        sound_list += [sound]
        if animal=='what':
            break
    
    fox = [x for x in noise if x not in sound_list]
    print(*fox)