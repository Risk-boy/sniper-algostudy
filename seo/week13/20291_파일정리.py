# 자료구조
# 문자열
# 정렬

# 시간 단축은 sys

from collections import Counter
import sys

n = int(input())
file_list = []
for i in range(n):
    file_name = sys.stdin.readline().rstrip()
    file_list += [file_name.split('.')[1]]

file = Counter(file_list)

file = sorted(file.items())
for name in file:
    print(name[0], name[1], end='\n')