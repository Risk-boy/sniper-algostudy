import sys

[n, m] = map(int, sys.stdin.readline().rstrip().split())

cards = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

max_m = 0

for i in range(n):
    total_temp_1 = cards[i]
    if total_temp_1 > m:
        break
    
    for j in range(i+1, n):
        total_temp_2 = total_temp_1 + cards[j]
        if total_temp_2 > m:
            break
        
        for k in range(j+1, n):
            total = total_temp_2 + cards[k]
            
            if total > m:
                break
            else:
                if total > max_m:
                    max_m = total
print(max_m)