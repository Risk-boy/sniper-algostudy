import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
room = [1 for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    for i in range(x, y):
        room[i] = 0
        
print(room[1:].count(1))
        