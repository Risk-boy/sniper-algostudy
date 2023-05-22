import sys

[n, m] = list(map(int, sys.stdin.readline().rstrip().split()))

a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

# print(*sorted(a+b))

result = []

a_i = 0
b_i = 0

while a_i < n and b_i < m:
    
    if a[a_i] < b[b_i]:
        result.append(a[a_i])
        a_i += 1
    else:
        result.append(b[b_i])
        b_i += 1
        
if a_i == n:
    result += b[b_i:]
else:
    result += a[a_i:]
    
print(*result)