import sys
input = sys.stdin.readline 


def dfs(cur, prev):
    global check
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt, cur)
        else:
            if nxt != prev:
                check = False
                return 
    return 


cnt = 1
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)
    answer = 0
    for i in range(1, n + 1):
        check = True
        if not visited[i]:
            dfs(i, -1)
            if check:
                answer += 1
                
    if answer > 1:
        print(f"Case {cnt}: A forest of {answer} trees.")
    elif answer == 1:
        print(f"Case {cnt}: There is one tree.")
    else:
        print(f"Case {cnt}: No trees.")
    cnt += 1