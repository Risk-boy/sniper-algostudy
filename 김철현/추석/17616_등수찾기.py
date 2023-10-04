import sys
input = sys.stdin.readline 


def solve(cur, ls):
    global cnt
    visited[cur] = True
    for nxt in ls[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            cnt += 1
            solve(nxt, ls)
    return

N, M, X = map(int, input().split())
up = [[] for _ in range(N + 1)]
down = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    down[A].append(B)
    up[B].append(A)


# up 위로 몇명인지 세서 cnt + 1 가 최고 등수
visited = [0] * (N + 1)
cnt = 0
solve(X, up)
print(1 + cnt, end=" ")
# down 아래 몇명인지 세서 n - cnt 가 최저 등수
visited = [0] * (N + 1)
cnt = 0
solve(X, down)
print(N - cnt)