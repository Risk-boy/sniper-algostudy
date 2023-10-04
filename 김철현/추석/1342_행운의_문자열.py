import sys
input = sys.stdin.readline 


def solve(idx, prev):
    global ans
    if idx == n:
        ans += 1
        
    for i in range(26):
        if count[i] == 0 or prev == i:
            continue
        count[i] -= 1
        solve(idx + 1, i)
        count[i] += 1
        
    return 


s = list(input().rstrip())
n = len(s)

count = [0] * 26
for x in s:
    count[ord(x) - ord("a")] += 1

ans = 0
solve(0, -1)
print(ans)