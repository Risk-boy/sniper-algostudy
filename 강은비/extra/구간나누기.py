import sys
  
n, m = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
dp1 = [[-float("inf") for _ in range(m+1)] for _ in range(n)]  #i번째 포함
dp2 = [[-float("inf") for _ in range(m+1)] for _ in range(n)]  #i번째 포함x

dp2[0][0]=0
dp1[0][1] = nums[0]   #첫 구간 

for i in range(1, n):
    dp2[i][0] = 0    #아무것도 포함되지 않음
    for j in range(1, m+1):
        #nums[i]를 포함o -> i전까지 j개의 구간(구간 잇기) or i전까지 j-1개의 구간(구간 생성)
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j-1])+nums[i]  
        #nums[i]를 포함x -> i전까지 j개의 구간 그대로 
        dp2[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        

print(max(dp1[n-1][m], dp2[n-1][m]))       
