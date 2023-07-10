import sys 
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

data = [input() for _ in range(N)]
answer = 0
for i in data:
    tmp = defaultdict(list)
    for j in range(len(i)):
        tmp[i[j]].append(j)
    
    tmp_ = len(tmp.keys())
    tmp_count = 0 
    for key in tmp.keys():
        length = len(tmp[key])
        start = tmp[key][0]
        end = tmp[key][-1]
        if end-start+1 == length:
            tmp_count += 1 
    if tmp_count == tmp_:
        answer += 1 
print(answer)

####### 
def func(x):
    A = list(x)
    B = []
    C = []
    for i in A:
        if i in B:
            pass
        else:
            B.append(i)
    for j in B:
        lst = []
        for k in range(len(A)):
            if j == A[k]:
                lst.append(k)
        C.append(lst)
    cnt = 0
    for i in range(len(C)):
        for j in range(i+1,len(C)):
            if (min(C[j])<min(C[i])<max(C[j])) or (min(C[j])<max(C[i])<max(C[j])) or ((min(C[i])<max(C[j])<max(C[i]))):
                cnt += 1
    return cnt

n = int(input())
count = 0
for _ in range(n):
    if func(input()) == 0:
        count += 1
    else:
        pass
print(count)
