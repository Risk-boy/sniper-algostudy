import sys
import re

def input():
    return sys.stdin.readline().rstrip()

var = input()

java_var = var[0].islower() and "_" not in var # 첫 글자가 소문자이고 "_"가 없어야한다.
cpp_var = var.islower() and re.search(r'_', var) is not None # 전체 글자가 소문자이고, '_'가 존재해야한다.

if java_var:
    result = ""
    for ind, char in enumerate(var):
        if char.isupper() and ind > 0 :
            result += "_"
        result += char.lower()
    print(result)
elif cpp_var:
    words = var.split("_")
    if any(word=="" for word in words): # '__' 가 있거나 '_asd', 'asd_'처럼 맨 앞과 뒤에 _가 있을 수 있어서 예외처리
        print("Error!")
    else:
        result = words[0] + "".join(word.capitalize() for word in words[1:])
        print(result)
else:
    print("Error!")



