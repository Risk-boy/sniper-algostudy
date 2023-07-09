# 구현

import sys

n = int(input())

cnt = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()

    spells = []
    devide = []

    alp = ""
    for i in word:
        spells += [i]
        if alp != i:
            alp = i
            devide += alp

    if len(set(spells)) == len(devide):
        cnt += 1

print(cnt)


# n = int(input())
# cnt = 0

# for i in range(n):
#     s = input()
#     for j in range(len(s)-1):
#         if s[j] != s[j+1]:
#             tmp = s[j+1:]
#             if s[j] in tmp:
#                 cnt -= 1
#                 break
#     cnt += 1
# print(cnt)
