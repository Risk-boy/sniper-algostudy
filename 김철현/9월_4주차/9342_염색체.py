import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    s = list(input().rstrip())
    n = len(s)
    if n < 3:
        print("Good")
        continue
    cur = s[0]
    for i in range(1, n):
        if s[i] not in "ABCDEF":
            print("Good")
            break
        if cur == "A":
            if s[i] != "A" and s[i] !="F":
                print("Good")
                break
        elif cur == "F":
            if s[i] != "F" and s[i] != "C":
                print("Good")
                break
        elif cur == "C":
            if s[i] != "C" and i != n - 1:
                print("Good")
                break
        cur = s[i]
    else:
        print("Infected!")
