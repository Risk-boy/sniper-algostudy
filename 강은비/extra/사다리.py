import sys
'''
def move(cur):
    for i in range(cur, n):
        if dir[i]:
            if left[i] == 0:
                left[i] += 1
                right[i] += 1
                dir[i] = 0
            else:
                left[i] -= 1
                right[i] -= 1
        else:
            if right[i] == l:
                left[i] -= 1
                right[i] -= 1
                dir[i] = 1
            else:
                left[i] += 1
                right[i] += 1

n, l = map(int, sys.stdin.readline().split())
left = [0 for _ in range(n)]
right = [0 for _ in range(n)]
dir = [0 for _ in range(n)]

for i in range(n):
    length, d = map(int, sys.stdin.readline().split())
    left[i] = l - length if d else 0
    right[i] = l if d else length
    dir[i] = d
 
t = 0
cur = 0
while True:
    while cur < n - 1:
        cl, cr = left[cur], right[cur]
        ul, ur = left[cur + 1], right[cur + 1]
        if ul <= cl <= ur or ul <= cr <= ur or (cl <= ul <= cr and cl <= ur <= cr):
            cur += 1
        else:
            break
        
    move(cur)
    
    if cur == n - 1:
        print(t)
        break
    
    t += 1
'''    
n, t = map(int, sys.stdin.readline().split())
maxd = 0
prev_l = None
prev_d = None
for _ in range(n):
    l, d = map(int, sys.stdin.readline().split())
    if prev_d != None and prev_d != d:    #방향이 다를 때만
        maxd = max(maxd, t - l - prev_l)  #사이 간격
        
    prev_l, prev_d = l, d 
    
print(maxd >> 1)
