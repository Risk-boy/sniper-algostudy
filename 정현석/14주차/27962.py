import sys

n = int(sys.stdin.readline().rstrip())
orange = sys.stdin.readline().rstrip()

ans = 'NO'

for i in range(n):
    left = orange[:i]
    right = orange[-i:]
    
    count = 0
    for j in range(i):
        if left[j] != right[j]:
            count += 1
        if count > 1:
            break
        
    if count == 1:
        ans = 'YES'
        break

print(ans)