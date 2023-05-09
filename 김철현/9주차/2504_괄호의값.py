import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def check():
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        elif x == "[":
            stack.append(x)
        elif x == ")":
            if stack and stack[-1] == "(":
                    stack.pop()
            else:
                return False
        elif x == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

def solve():
    global idx
    idx += 1
    if s[idx] in dict:
        idx += 1
        return dict[s[idx - 1]]

    temp = 0
    while True:
        if s[idx] in dict:
            break
        temp += solve()

    idx += 1
    return temp * dict[s[idx - 1]]


s = list(input().rstrip())
if not check():
    print(0)
    exit()
dict = {")": 2, "]": 3}
answer = 0
idx = 0
while idx < len(s):
    answer += solve()

print(answer)