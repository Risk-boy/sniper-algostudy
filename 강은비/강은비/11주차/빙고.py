import sys

def check():
    global bingo
    for i in range(5):
        if not h[i] and "".join(visit[i])=="11111":
            bingo+=1
            h[i]=1
            
    for i in range(5):
        if not v[i] and "".join([visit[j][i] for j in range(5)])=="11111":
            bingo+=1
            v[i]=1
            
    for i in range(2):
        if not d[i] and ((i==0 and "".join([visit[i][i] for i in range(5)])=="11111") or (i==1 and "".join([visit[i][4-i] for i in range(5)])=="11111")):
            bingo+=1
            d[i]=1
            
bingo=0           
nums=dict()  
h=[0 for _ in range(5)]
v=[0 for _ in range(5)]
d=[0, 0]
for i in range(5):
    for j, x in enumerate(sys.stdin.readline().split()):
        nums[x]=(i, j)
visit=[["0" for _ in range(5)] for _ in range(5)]

q=[]
for i in range(5):
    q+=sys.stdin.readline().split()
    
for i, k in enumerate(q, 1):
    x, y=nums[k]
    visit[x][y]="1"
    if i>=12:
        check()
        if bingo>=3:
            print(i)
            sys.exit()
    
        