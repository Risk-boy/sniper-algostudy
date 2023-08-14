import sys
input = sys.stdin.readline 


n = int(input())
arr = list(map(int, input().split()))
two = 0
rest = 0
for x in arr:
    two += x // 2
    rest += x % 2

if rest > two:
    print("NO")
else:
    if sum(arr) % 3 == 0:
        print("YES")
    else:
        print("NO")