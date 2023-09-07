import sys
input = sys.stdin.readline 


def push(ls):
    for i in range(len(ls) - 1, -1 , -1):
        result.append(ls[i])
    return []


s = list(input().rstrip())
tag = False
result = []
word = []
for i in range(len(s)):
    if s[i] == "<":
        tag = True
        if word:
            word = push(word)
        result.append("<")
    elif s[i] == ">":
        tag = False
        result.append(">")
    elif s[i] == " ":
        if not tag:
            if word:
                word = push(word)
            result.append(" ")
        else:
            result.append(s[i])
    else:
        if not tag:
            word.append(s[i])
        else:
            result.append(s[i])

if word:
    push(word)

print("".join(result))