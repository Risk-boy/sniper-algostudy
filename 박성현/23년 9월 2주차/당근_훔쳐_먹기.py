import sys

n, t = map(int, sys.stdin.readline().split())
carrots = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)] # w(현재), p(증가)
carrots.sort(key = lambda x: x[1])

result = 0
feeded_days = t-n
for w, p in carrots:
    result += (w + p*feeded_days)
    feeded_days += 1

print(result)