import sys

n = int(sys.stdin.readline())
photo = {}
t = int(sys.stdin.readline())
rec = list(map(int, sys.stdin.readline().split()))
for i, s in enumerate(rec):
    if not photo.get(s, None):
        if len(photo)>=n:
            k = sorted(photo.items(), key = lambda x: x[1])[0][0]
            photo.pop(k)
        photo[s] = [0, i] 
    else:
        photo[s][0]+=1
        
print(*sorted(photo.keys()))
    

            
            