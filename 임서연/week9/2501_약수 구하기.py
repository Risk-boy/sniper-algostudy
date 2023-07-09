# 수학
# 브루트포스 알고리즘

n, k = map(int, input().split())

num = []
for i in range(1, n+1):
    if n%i == 0:
        num.append(i)
    else:
        pass

num.sort()

if len(num) < k:
    print(0)
else:
    ans = num[k-1]
    print(ans)