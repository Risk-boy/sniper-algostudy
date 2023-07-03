import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    
    s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    s.sort()
    m = s[0][1]
    
    cnt = 0
    for x, y in s:
        if y <= m:
            m = y
            cnt += 1
            
    print(cnt)
    
    
    