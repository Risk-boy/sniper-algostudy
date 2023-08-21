import sys

def cal(a, b, op):
    if op == "+":
        return str(int(a)+int(b))
    elif op == "-":
        return str(int(a)-int(b))
    else:
        return str(int(a)*int(b))
        

def find(x, idx):
    if idx==n-1:
        answer.append(int(x))
        return 

    if idx+2<n:
        find(cal(x, s[idx+2], s[idx+1]), idx+2)
        
    if idx+4<n:
        p = cal(s[idx+2], s[idx+4], s[idx+3])
        find(cal(x, p, s[idx+1]), idx+4)
        
n = int(sys.stdin.readline())
s = list(sys.stdin.readline().rstrip())
answer = []

find(s[0], 0)
answer.sort()

print(answer[-1])
