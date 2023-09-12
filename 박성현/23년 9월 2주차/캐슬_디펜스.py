import sys 
import copy
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def move_enemy(enemy_pos, N):
    moved_enemy_pos = set()
    for x, y in enemy_pos:
        if x == N-1:  # 성벽까지 도달했다면
            continue
        else:
            moved_enemy_pos.add((x+1, y))
    return moved_enemy_pos

def possible_enemy(y, enemy_pos, N, D):
    result = []
    for dx, dy in enemy_pos:
        D_x = abs(dx - (N))
        D_y = abs(dy - y)
        dis = D_x + D_y
        if dis <= D:
            result.append((dx, dy, dis))
    if len(result) >= 1:
        result.sort(key=lambda x: (x[2], x[1]))
        return result[0]
    else:
        return None

N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

enemy_pos = {(i, j) for i in range(N) for j in range(M) if graph[i][j] == 1}

max_removed_enemy = 0
from pprint import pprint
for comb in combinations(range(M), 3):
    # print(f'this times comb:{comb}')
    current_enemy_pos = copy.deepcopy(enemy_pos)
    removed_enemy = 0
    while current_enemy_pos:
        targets = set()
        for archer in comb:
            target = possible_enemy(archer, current_enemy_pos, N, D)
            if target:
                targets.add(target[:2])
        removed_enemy += len(targets)
        # print(len(targets))
        current_enemy_pos -= targets  # 공격 당한 적을 제거
        current_enemy_pos = move_enemy(current_enemy_pos, N)  # 적을 이동시킴
        # pprint(current_enemy_pos)
    max_removed_enemy = max(max_removed_enemy, removed_enemy)

print(max_removed_enemy)