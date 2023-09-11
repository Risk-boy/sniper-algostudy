import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10 ** 6)


def solve(cur, prev):
    for nxt in graph[cur]:
        if nxt != prev:
            parent[nxt] = cur
            solve(nxt, cur)
    
    return


n = int(input())
parent = [-1 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

solve(1, -1)
for x in parent[2:]:
    print(x)