import sys

[n, x] = list(map(int, sys.stdin.readline().rstrip().split()))
visits = list(map(int, sys.stdin.readline().rstrip().split()))

max_visits = sum(visits[:x])
prev_visits = max_visits
count = 1

for i in range(1, n - x + 1):
    curr_visits = prev_visits - visits[i-1] + visits[i+x-1]
    if curr_visits > max_visits:
        max_visits = curr_visits
        count = 1
    elif curr_visits == max_visits:
        count += 1
    
    prev_visits = curr_visits
        
if max_visits == 0:
    print('SAD')
else:
    print(max_visits)
    print(count)
    