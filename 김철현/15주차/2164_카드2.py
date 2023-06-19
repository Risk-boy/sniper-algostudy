import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque([i for i in range(1, n + 1)])

while len(q) != 1:
    q.popleft()
    q.rotate(-1)
    

print(q.popleft())