import sys
from collections import defaultdict

score=defaultdict(lambda : [0,0,0])

n=int(sys.stdin.readline())
for _ in range(n):
    s=list(map(int, sys.stdin.readline().split()))
    for i in range(3):
        score[i][s[i]-1]+=s[i]
        
score=sorted(score.items(), key=lambda x: (-sum(x[1]), -x[1][2], -x[1][1]))
m=sum(score[0][1])

if score[0][1][2]==score[1][1][2] and score[0][1][1]==score[1][1][1]:
    print(0, m)
else:
    print(score[0][0]+1, m)
    