import sys
input = sys.stdin.readline 


arr = list(input().rstrip())
cnt = 0 
stack = []
answer = 0
for x in arr:
    if x == "(":
        stack.append(x)
        cnt += 1
    elif x == ")":
        cnt -= 1
        if stack[-1] == ")":
            answer += 1
        else:
            answer += cnt
        stack.append(x)
        
print(answer)