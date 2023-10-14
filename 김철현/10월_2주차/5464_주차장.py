import sys
input = sys.stdin.readline 
from collections import deque 


N, M = map(int, input().split())
pay = [int(input()) for _ in range(N)]
weight = [0] + [int(input()) for _ in range(M)]
visited = [0] * N
q = deque()
ans = 0
for _ in range(2 * M):
    n = int(input())
    if n > 0:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = n
                ans += pay[i] * weight[n]
                break
        else:
            q.append(n)
    else:
        for i in range(N):
            if visited[i] == -n:
                visited[i] = 0
                if q:
                    x = q.popleft()
                    visited[i] = x
                    ans += pay[i] * weight[x]
                break

print(ans)