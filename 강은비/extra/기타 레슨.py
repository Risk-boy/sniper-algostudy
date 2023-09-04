import sys

n, m = map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))
answer = []
l = max(time)
r = sum(time)

while l<=r:
    mid = (l+r) // 2
    tmp = 0
    cnt = 1
    for i in range(n):
        if tmp + time[i] <= mid:
            tmp += time[i]
        else:
            cnt+=1
            tmp = time[i]
            
    if cnt <= m:
        answer.append(mid)
        r = mid-1
    elif cnt > m:
        l = mid + 1
        
answer.sort()
print(answer[0])