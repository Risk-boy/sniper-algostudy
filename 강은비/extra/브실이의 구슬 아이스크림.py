import sys
balls = {}
n = int(sys.stdin.readline())

for x in map(int, sys.stdin.readline().split()):
    balls[x] = balls.get(x, 0) + 1
    
q = int(sys.stdin.readline())
for _ in range(q):
    an, *a = list(map(int, sys.stdin.readline().split()))
    bn, *b = list(map(int, sys.stdin.readline().split()))
    t = {}
    for x in a:
        if balls.get(x, 0) >= t.get(x, 0) + 1:
            t[x] = t.get(x, 0) + 1
        else:
            break
    else:
        for k, v in t.items():
            balls[k] -= v
            if balls[k] == 0:
                balls.pop(k)
        for x in b:
            balls[x] = balls.get(x, 0) + 1
            
print(sum(balls.values()))
if balls:
    answer = [k for k, v in balls.items() for _ in range(v)]
    print(*answer)
    
