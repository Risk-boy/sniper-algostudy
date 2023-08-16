# 구현
# 시뮬레이션
# room = [[]]*100 // 100개 [] 모두 같은 주소를 공유하게 된다 - 하나 변하면 다같이 변함

import sys

p, m = map(int, sys.stdin.readline().split())

player = {}
room = [[] for _ in range(p)]
for i in range(p):
    l, n = sys.stdin.readline().split()
    l = int(l)
    player[n] = l
    for r in room:
        if len(r)==0:
            r += [n]
        else:
            rl = player[r[0]]
            if l<=rl+10 and l>=rl-10 and len(r)<m:
                r += [n]
            else:
                continue
        break

for r in room:
    if len(r)==0:
        pass
    elif len(r)!=m:
        print('Waiting!')
        r.sort()
        for i in r:
            print(player[i], i)
    else:
        print('Started!')
        r.sort()
        for i in r:
            print(player[i], i)