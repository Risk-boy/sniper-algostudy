# 구현

import sys

n = int(input())

student = []
for i in range(n):
    name, dd, mm, yy = sys.stdin.readline().split()
    dd, mm, yy = int(dd), int(mm), int(yy)
    student += [(yy, mm, dd, name)]

print(max(student)[3])
print(min(student)[3])