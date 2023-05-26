import sys

nums=[int(sys.stdin.readline()) for _ in range(10)]
answer=0

for i in range(10):
    if abs(answer-100)>=abs(answer+nums[i]-100):
        answer+=nums[i]
    else:
        break
print(answer)
    
        
        
