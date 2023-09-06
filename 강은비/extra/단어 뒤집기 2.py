import sys

s = sys.stdin.readline().rstrip()
answer = ""
tmp = ""
tag = False
for x in s:
    if x == "<":
        answer += tmp[::-1]
        tmp = ""
        tag = True
        
    if tag:
        answer += x
        if x == ">":
            tag = False
    else:
        if x == " ":
            answer += tmp[::-1]+x
            tmp = ""
        else:
            tmp += x
    
print(answer+tmp[::-1])
    
        