# 자료구조
# 문자열
# 정렬

from collections import Counter

n = int(input())
file_list = []
for i in range(n):
    file_name = input()
    file_list += [file_name.split('.')[1]]

file = Counter(file_list)

file = sorted(file.items())
for name in file:
    print(name[0], name[1], end='\n')