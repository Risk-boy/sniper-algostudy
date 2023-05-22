import sys
input = sys.stdin.readline 


n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
visited = [False] * n
cur = 0
cnt = 0

while True:
    visited[cur] = True
    cnt += 1
    cur = arr[cur]

    if visited[k]:
        print(cnt - 1)
        break
    if visited[cur]:
        print(-1)
        break

