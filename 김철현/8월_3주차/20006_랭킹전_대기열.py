import sys
input = sys.stdin.readline 


p, m = map(int, input().split())
ls = []
for _ in range(p):
    lv, name = input().split()
    lv = int(lv)
    if not ls:
        ls.append([(lv, name)])
    else:
        for x in ls:
            if x[0][0] - 10 <= lv <= x[0][0] + 10 and len(x) < m:
                x.append((lv, name))
                break
        else:
            ls.append([(lv, name)])
                
            

for candi in ls:
    if len(candi) == m:
        print("Started!")
        candi.sort(key=lambda x: x[1])
        for x in candi:
            print(x[0], x[1])
    else:
        print("Waiting!")
        candi.sort(key=lambda x: x[1])
        for x in candi:
            print(x[0], x[1])