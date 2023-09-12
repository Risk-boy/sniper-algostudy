import sys
def input():
    return sys.stdin.readline().rstrip()

def can_fold(s):
    cur = list(s)

    while len(cur) >= 3:
        for i in range(2, len(cur), 2):
            if cur[i-2] == cur[i]:
                return False

        nxt = cur[1::2]
        cur = nxt

    return True

T = int(input())
for _ in range(T):
    pat = str(input())

    if can_fold(pat):
        print("YES")
    else:
        print("NO")