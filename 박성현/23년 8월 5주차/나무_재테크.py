import sys 
def input():
    return sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
tree = [[[] for _ in range(n)] for _ in range(n)]

feed = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

food = [[5] * n for _ in range(n)]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def grow(food, tree):
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead_tree =[], 0
                for t in tree[i][j]:
                    if food[i][j] >= t:
                        food[i][j] -= t
                        t += 1
                        temp_tree.append(t)
                    else:
                        dead_tree += t // 2
                food[i][j] += dead_tree
                tree[i][j] = []
                tree[i][j].extend(temp_tree)

    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) == 0:
                continue
            for p in range(len(tree[i][j])):
                if (tree[i][j][p] % 5 == 0):
                    x, y = i, j
                    for q in range(8):
                        nx = x + dx[q]
                        ny = y + dy[q]
                        if 0 <= nx < n and 0 <= ny < n:
                            tree[nx][ny].append(1)

    for i in range(n):
        for j in range(n):
            food[i][j] += feed[i][j]


for _ in range(k):
    grow(food, tree)

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer)