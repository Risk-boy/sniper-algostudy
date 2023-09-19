import sys
input = sys.stdin.readline 


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse = True)
B.sort()
ans = 0
for i in range(min(N, M)):
    if A[i] > B[i]:
        ans += (A[i] - B[i])
    else:
        break
    
print(ans)