import sys
input = sys.stdin.readline 


n = int(input())

result = set()
target = "ChongChong"
for _ in range(n):
    a, b = input().split()
    if a == target or b == target:
        result.add(a)
        result.add(b)
    else:
        if target in result and (a in result or b in result):
            result.add(a)
            result.add(b)

print(len(result))