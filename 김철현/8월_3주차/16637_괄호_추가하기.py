import sys
input = sys.stdin.readline 


def cal(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    else:
        return num1 * num2
    
    
def solve(num, cnt):
    global max_v
    if cnt == n:
        max_v = max(max_v, num)
        return
    
    solve(cal(num, int(arr[cnt + 1]), arr[cnt]), cnt + 2)
    if cnt + 2 < n:
        solve(cal(num, cal(int(arr[cnt + 1]), int(arr[cnt + 3]), arr[cnt + 2]), arr[cnt]), cnt + 4)
        

n = int(input())
arr = list(input().rstrip())
max_v = -int(2e31)
solve(int(arr[0]), 1)
print(max_v)