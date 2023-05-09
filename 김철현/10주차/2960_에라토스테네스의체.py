import sys, math
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
prime = [True] * (n + 1)

cnt = 0
for i in range(2, n + 1):
    if prime[i]:
        prime[i] = False
        cnt += 1
        if cnt == k:
            print(i)
            break
        j = 2
        while i * j <= n:
            if prime[i * j]:
                prime[i * j] = False
                cnt += 1
                if cnt == k:
                    print(i * j)
                    exit()
            j += 1