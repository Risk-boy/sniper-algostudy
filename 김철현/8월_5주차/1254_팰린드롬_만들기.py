import sys
input = sys.stdin.readline 


s = input().rstrip()
n = len(s)
rest = ""

if s == s[::-1]:
    print(n)
else:
    for i in range(n):
        rest = s[i] + rest
        x = s + rest
        if x == x[::-1]:
            print(len(x))
            break