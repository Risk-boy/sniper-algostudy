import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline



def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


v, e = map(int, input().split())
arr = []
parent = [i for i in range(v + 1)]
answer = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    arr.append([c, a, b])

arr.sort()

for cost, x, y in arr:
    x = find(x)
    y = find(y)

    if x != y:
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

        answer += cost

print(answer)





