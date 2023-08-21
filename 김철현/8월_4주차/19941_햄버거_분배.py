import sys
input = sys.stdin.readline


n, k = map(int, input().split())
arr = list(input().rstrip())
visited = [False] * n
cnt = 0
for i in range(n):
    if arr[i] == "P":
        for j in range(max(0, i - k), min(i + k + 1, n)):
            if arr[j] == "H" and not visited[j]:
                cnt += 1
                visited[j] = True
                break
print(cnt)