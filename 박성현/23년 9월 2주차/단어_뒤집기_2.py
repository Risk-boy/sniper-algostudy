s = input()
is_tag = False
word = ''
result = ''

for char in s:
    if char == '<':
        is_tag = True
        result += word[::-1] + '<'
        word = ''
    elif char == '>':
        is_tag = False
        result += '>'
    elif char == ' ':
        if is_tag:
            result += ' '
        else:
            result += word[::-1] + ' '
            word = ''
    else:
        if is_tag:
            result += char
        else:
            word += char

result += word[::-1]  # 마지막 단어 추가
print(result)