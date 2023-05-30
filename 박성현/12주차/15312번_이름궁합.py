import sys
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip()


num_list = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

def f(x,y):
    tmp = []
    for i in range(len(x)):
        tmp.append(num_list[abs(ord(x[i])-65)])
        tmp.append(num_list[abs(ord(y[i])-65)])
    return tmp

def sol(x,n:int) -> int:    
    if n == 2:
        print("now, n is 2", x)
        return x
    else:
        y = []
        for i in range(len(x)-1):
            y.append((x[i]+x[i+1])%10)
            print("y is here:", y)
        return sol(y, n-1)


X = input()
Y = input()

tmp_ans = sol(f(X,Y), len(f(X,Y)))
print(''.join(map(str, tmp_ans)))
