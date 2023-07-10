import sys

def check(s):
    ch = set()
    for i in range(len(s)):
        if i == 0:
            ch.add(s[i])
        else:
            if s[i] != s[i-1] and set(s[i])&ch:
                return False
            else:
                ch.add(s[i])
    return True
                


n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

cnt = 0
for x in words:
    if check(x):
        cnt+=1
print(cnt)
    