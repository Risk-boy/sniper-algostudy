import sys
input = sys.stdin.readline 


n, k, q = map(int, input().split()) # 학생 수 / 은호 학년 / 질문 수
arr = [0] + list(map(int, input().split()))
question = list(map(int, input().split()))
dp = [0] * (n + 1) 

cnt = 0
prev = 0
for i in range(1, n + 1):
    if arr[i] != k:
        cnt += 1
        dp[i] = dp[i - 1] + cnt
    else:
        dp[i] = dp[i - 1]
        cnt = 0


for x in question:
    print(dp[x])