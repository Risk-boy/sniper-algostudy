import sys
input = sys.stdin.readline 


n = int(input())
s = input().rstrip()
flag = True
for i in range(1, n + 1):
    front = s[0:i]
    back = s[n - i:n]
    cnt = 0
    for j in range(i):
        if front[j] != back[j]:
            cnt += 1
    if cnt == 1:
        flag = False
        print("YES")
        break

if flag:
    print("NO")