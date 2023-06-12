import sys
input = sys.stdin.readline 


n, m, k = map(int, input().split())
visited = [False] * n 
for _ in range(m):
    idx = int(input())
    visited[idx] = True

for _ in range(k):
    arr = []
    for i in range(n):
        arr.append(visited[i - 1] ^ visited[(i + 1) % n])
        
    visited = arr
    

print(sum(visited))