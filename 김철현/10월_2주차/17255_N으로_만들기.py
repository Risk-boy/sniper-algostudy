import sys
input = sys.stdin.readline 


def solve(x):
    global ans
    if len(x) == len(N):
        if N == x:
            ans += 1
        return 

    for i in range(10):
        if not check[i]:
            continue
        
        i = str(i)
        left = i + x
        right = x + i
        
        if left != right:
            solve(left)
            solve(right)
        else:
            solve(left)


N = input().rstrip()
check = [False] * 10

for i in range(len(N)):
    check[int(N[i])] = True

ans = 0
solve("")
print(ans)