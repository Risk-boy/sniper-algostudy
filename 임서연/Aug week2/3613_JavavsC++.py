# 구현
# 문자열

import sys

var = input()

result = ''
if var[0].isupper() or var[0]=='_' or var[-1]=='_':     # 대문자, _로 시작하거나 끝나는 경우 
    print('Error!')
elif '_' in var:
    var = var.split('_')
    if "" in var:   # _ 연속 2번
        print('Error!')
    else:
        for i in var:
            if i.islower()==False:  # 대문자 섞인 경우
                print('Error!')
                break
        else:
            for j in range(len(var)):
                if j==0:
                    result += var[j]
                else:
                    result += var[j][0].upper() + var[j][1:]
            print(result)
else:
    for i in var:
        if i.isupper():
            result += '_' + i.lower()
        else:
            result += i
    print(result)
