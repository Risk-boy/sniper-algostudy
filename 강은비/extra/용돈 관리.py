import sys

n, m = map(int, sys.stdin.readline().split())
money = [int(sys.stdin.readline()) for _ in range(n)]
answer = -1
l = max(money)
r = sum(money)

while l<=r:
    mid = (l+r)//2
    rest = mid
    cnt = 1    
    for i in range(n):
        if rest<money[i]:
            rest = mid
            cnt+=1
        rest-=money[i] 
        
    if cnt>m:
        l = mid+1
    else:
        answer = mid
        r = mid-1 
        
print(answer)