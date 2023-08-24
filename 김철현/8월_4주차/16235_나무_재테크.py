import sys
input = sys.stdin.readline
from collections import deque


n, m, k = map(int, input().split())
energy = [list(map(int, input().split())) for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]
rest = [[5] * n for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for i in range(n):
    for j in range(n):
        trees[i][j] = deque(sorted(trees[i][j]))

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
    # 봄, 여름
    for i in range(n):
        for j in range(n):
            cnt = 0
            length = len(trees[i][j])
            for idx in range(0, length):
                if rest[i][j] < trees[i][j][idx]:
                    break
                else:
                    rest[i][j] -= trees[i][j][idx]
                    trees[i][j][idx] += 1
                    cnt += 1
                
            for _ in range(length - cnt):
                die = trees[i][j].pop()
                rest[i][j] += die // 2
    
    # 가을, 겨울
    for i in range(n):
        for j in range(n):
            for idx in range(len(trees[i][j])):
                if trees[i][j][idx] % 5 == 0:
                    for l in range(8):
                        ni, nj = i + dr[l], j + dc[l]
                        if 0 <= ni < n and 0 <= nj < n:
                            trees[ni][nj].appendleft(1)
            rest[i][j] += energy[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])

print(answer)
