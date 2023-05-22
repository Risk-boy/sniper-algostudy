import sys
input = sys.stdin.readline 


s = list(input().rstrip())
result = []
for i in range(len(s)):
    if i == 0:
        result.append(s[i])
    else:
        if s[i] != s[i - 1]:
            result.append(s[i])

cnt_0 = result.count("0")
cnt_1 = result.count("1")

print(min(cnt_0, cnt_1))