import sys

n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
dp=[x for x in a]  #수열 길이가 1 일때 

for i in range(n):
    for j in range(i):
        if a[j]<a[i]:   #i에서 가능한 수열의 최대 값
            dp[i]=max(dp[i], dp[j]+a[i])  #j까지 수열의 합+자기 자신
            
print(max(dp))
       