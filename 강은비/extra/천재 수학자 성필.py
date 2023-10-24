import sys

def cal(x, o, y):
    if o == "+":
        return x + y
    elif o == "-":
        return x - y 
    elif o == "*":
        return x * y
    else:
        return x // y

input = sys.stdin.readline
s = list(input().rstrip())
num = [s[0]]
for i in range(1, len(s)):
    if s[i].isdigit():
        num.append(s[i])
        continue
    
    x = num.pop()
    y = num.pop()
    num.append(cal(int(y), s[i], int(x)))
    
print(num.pop())
        
    
    
    
    
