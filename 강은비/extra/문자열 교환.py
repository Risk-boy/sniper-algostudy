import sys

s = sys.stdin.readline().rstrip()
size = 0
for x in s:
    if x == "a":
        size += 1

answer = float("inf")
for i in range(len(s)):
    cnt = 0
    for j in range(i, i + size):
        if s[j % len(s)] == "b":
            cnt += 1
    answer = min(cnt, answer)
            
print(answer)
            
        