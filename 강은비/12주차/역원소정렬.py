import sys

answer=[]

n, *nums=sys.stdin.readline().split()
while int(n)>len(nums):
    nums+=sys.stdin.readline().split()
    
for i in range(int(n)):
    answer.append(int(nums[i][::-1]))
answer.sort()

for x in answer:
    print(x)
    
