import sys

n, k = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline().rstrip())
cnt = 0
for i in range(n):
    if s[i] == "P":
        for j in range(i-k, i+k+1):
            if 0<=j<n and s[j] == "H":
                s[j] = -1
                cnt+=1
                break
print(cnt)  
