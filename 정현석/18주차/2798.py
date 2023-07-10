import sys

[n, m] = map(int, sys.stdin.readline().rstrip().split())

cards = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

max_m = 0

for i in range(n):
    total_1 = cards[i]
    for j in range(i+1, n):
        total_2 = total_1 + cards[j]
        for k in range(j+1, n):
            total_3 = total_2 + cards[k]
            
            if total_3 <= m:
                if total_3 > max_m:
                    max_m = total_3
            else:
                break
print(max_m)