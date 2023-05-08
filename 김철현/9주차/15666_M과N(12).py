import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve(cnt):
    global answer
    if cnt == m:
        print(*answer)
        return

    for num in ls:
        if len(answer) == 0 or answer[-1] <= num:
            answer.append(num)
            solve(cnt + 1)
            answer.pop()



n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls = list(set(ls))
ls.sort()
answer = []
solve(0)
