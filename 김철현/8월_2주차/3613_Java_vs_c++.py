import sys
input = sys.stdin.readline 


s = input().rstrip()
n = len(s)
underline = False # 밑줄 확인용
cap = False # 대문자 확인용
error = False   # 에러 확인용
for i in range(n):
    x = s[i]
    if i == 0:  # 첫번째는 대문자, _ 오면 안됨!
        if x == "_":
            error = True
            break
        elif 65 <= ord(x) <= 90:
            error = True
            break
    elif i == n - 1:    # 마지막에는 _ 안됨!
        if x == "_":
            error = True
        elif 65 <= ord(x) <= 90:
            if underline:
                error = True
    else:    
        if x == "_":    # 밑줄인 경우
            if cap:
                error = True
                break
            underline = True
            if s[i - 1] == "_" or s[i + 1] == "_":
                error = True
                break
        elif 65 <= ord(x) <= 90:    # 대문자인 경우
            cap = True
            if underline:   # 이미 밑줄이면 에러
                error = True
                break
if error:
    print("Error!")
    exit()
    
if underline:
    temp = s.split("_")
    for i in range(1, len(temp)):
        temp[i] = temp[i].capitalize()
    print("".join(temp))
else:
    temp = []
    for i in range(n):
        if i == 0:
            temp.append(s[i])
        else:
            if 65 <= ord(s[i]) <= 90:
                temp.append("_")
                temp.append(s[i].lower())
            else:
                temp.append(s[i])
    for x in temp:
        print(x, end="")