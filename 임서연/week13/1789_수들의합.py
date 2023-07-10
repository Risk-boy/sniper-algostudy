# 수학
# 그리디

s = int(input())

i = 1
num = []
while i <= s:
    num += [i]
    s -= i
    i += 1

print(len(num))