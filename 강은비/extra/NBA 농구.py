import sys

input = sys.stdin.readline
n = int(input())
score1 = score2 = 0
res1 = res2 = 0
prev = 0

for i in range(n):
    x, t = input().split()
    x = int(x)
    m , s = map(int, t.split(":"))
    if score1 > score2:
        res1 += m * 60 + s - prev
    elif score1 < score2:
        res2 += m * 60 + s - prev
        
    if x == 1:
        score1 += 1
    else:
        score2 += 1
        
    prev = m * 60 + s
    
if score1 > score2:
    res1 += 48 * 60 - prev
elif score1 < score2:
    res2 += 48 * 60 - prev

print("{:02d}:{:02d}".format(*divmod(res1, 60)))    
print("{:02d}:{:02d}".format(*divmod(res2, 60)))       
        
        
