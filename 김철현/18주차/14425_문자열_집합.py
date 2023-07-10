import sys
input = sys.stdin.readline 


n, m = map(int, input().split())
words = set()
for _ in range(n):
    x = input()
    words.add(x)
cnt = 0
for _ in range(m):
    if input() in words:
        cnt += 1
print(cnt)