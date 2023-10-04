import sys
input = sys.stdin.readline 


N = int(input())
M = int(input())
room = [i for i in range(N + 1)]
cmd = [list(map(int, input().split())) for _ in range(M)]
cmd.sort(key=lambda x: (x[0], x[1]))
for a, b in cmd:
    x = min(a, room[a])
    for i in range(a, b + 1):
        room[i] = x

cnt = 0
for i in range(1, N + 1):
    if room[i] != room[i - 1]:
        cnt += 1

print(cnt)