import sys

nums=list(map(int, sys.stdin.readline().split()))
while True:
    flag=0
    for i in range(0, 4):
        if nums[i]>=nums[i+1]:
            nums[i], nums[i+1]=nums[i+1], nums[i]
            print(*nums)
            flag=1
    if not flag:
        break
            