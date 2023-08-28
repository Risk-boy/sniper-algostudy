import sys

s = sys.stdin.readline().rstrip()
cnt = 0
back = ""
i = 0
while s+back != (s+back)[::-1]:
    back = s[i]+back
    i+=1
print(len(s+back))