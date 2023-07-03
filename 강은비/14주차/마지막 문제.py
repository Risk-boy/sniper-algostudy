import sys

n=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
nums.sort()
answer=[]

for i in range(n-1):
    mid=(nums[i]+nums[i+1])//2  #사이에 있는 수들 중 난이도 차이의 최대
    if mid!=nums[i]:
        answer.append((mid, mid-nums[i]))  #난이도 차이

if not answer:
    print(-1)
else:
    answer.sort(key=lambda x: (-x[1]))
    print(answer[0][0])
