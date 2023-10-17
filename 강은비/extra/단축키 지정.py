import sys

input = sys.stdin.readline
short = {}
n = int(input())
for _ in range(n):
    s = input().rstrip()
    other = ""
    idx = -1
    for i in range(len(s)):
        if i == 0 or s[i - 1] == " ":
            if short.get(s[i].lower()):
                continue
            else:
                short[s[i].lower()] = 1
                print(f"{s[:i]}[{s[i]}]{s[i + 1:]}")
                break
        else:
            if s[i] == " ":
                continue
            if short.get(s[i].lower()):
                continue
            else:
                if not other:
                    other = s[i]
                    idx = i
    else:
        if not other:
            print(s)
        else:
            short[other.lower()] = 1
            print(f"{s[:idx]}[{other}]{s[idx + 1:]}")
    
        
    
    