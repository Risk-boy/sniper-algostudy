import sys

brackets = sys.stdin.readline().rstrip()

s = []
wrong = False

for b in brackets:
    if b == '(' or b == '[':
        s.append(b)
    else:
        temp = 0
        while True:
            if not s:
                wrong = True
                break

            left = s.pop()
            if type(left) == int:
                temp += left
            elif b == ')' and left == '(':
                if temp == 0:
                    s.append(2)
                    break
                else:
                    s.append(temp*2)
                    break
            elif b == ']' and left == '[':
                if temp == 0:
                    s.append(3)
                    break
                else:
                    s.append(temp*3)
                    break
            else:
                wrong = True
                break
        if wrong:
            break

if wrong or '(' in s or '[' in s or ')' in s or ']' in s:
    print(0)
else:
    print(sum(s))