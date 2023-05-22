import sys

seq = sys.stdin.readline().rstrip()

s = []
stick = 1
prev = seq[0]
total = 0

for c in seq[1:]:
    if c == '(':
        stick += 1
    else:
        if prev == '(':
            stick -= 1
            total += stick
        else:
            stick -= 1
            total += 1
    prev = c

print(total)