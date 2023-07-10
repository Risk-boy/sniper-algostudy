# 구현
# 반례 : 같은 반이었던 학생이 중복일 경우

import sys

n = int(input())
fir, sec, thr, fort, fift = [], [], [], [], []
for i in range(n):
    a, b, c, d, e = map(int, sys.stdin.readline().split())
    fir += [a]
    sec += [b]
    thr += [c]
    fort += [d]
    fift += [e]

student = []
for j in range(n):
    same = []
    for x in [fir, sec, thr, fort, fift]:
        same += [i for i, ele in enumerate(x) if ele==x[j]]
    cnt = len(set(same))
    student += [cnt]

print(student.index(max(student))+1)