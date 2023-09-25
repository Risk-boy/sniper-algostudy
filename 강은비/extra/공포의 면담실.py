import sys

input = sys.stdin.readline
n = int(input())
l = []
for _ in range(n):
    n, *s = list(map(int, input().split()))
    l.append(sum(s))
    
l.sort()
answer = 0
prev = 0
for x in l:
    prev += x
    answer += prev
print(answer)