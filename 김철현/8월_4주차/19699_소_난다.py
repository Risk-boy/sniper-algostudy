import sys
input = sys.stdin.readline


def solve(idx, total, cnt):
    if cnt == m:
        if prime[total]:
            result.add(total)
        return
    
    if idx == n:
        return
    
    solve(idx + 1, total, cnt)
    solve(idx + 1, total + arr[idx], cnt + 1)
    
    return


n, m = map(int, input().split())
arr = list(map(int, input().split()))

prime = [True] * 9001
for i in range(2, int(9001 ** 0.5) + 1):
    if prime[i]:
        j = 2
        while i * j <= 9000:
            prime[i * j] = False
            j += 1


result = set()
solve(0, 0, 0)
if result:
    result = sorted(list(result))
    print(*result)
else:
    print(-1)