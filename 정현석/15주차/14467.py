import sys

num_obs = int(sys.stdin.readline().rstrip())
obs = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num_obs)]

history = {}
count = 0

for o in obs:
    if o[0] not in history:
        history[o[0]] = o[1]
    else:
        if history[o[0]] != o[1]:
            count+=1
            history[o[0]] = o[1]
            
print(count)