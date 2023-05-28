import sys
input = sys.stdin.readline 


result = []
ls = list(input().rstrip().split())
n = int(ls[0])
for i in range(1, len(ls)):
    result.append(ls[i])
        
while len(result) != n:
    ls = list(input().rstrip().split())
    for x in ls:
        result.append(x)
    

total = []
for x in result:
    total.append(int(x[::-1]))

total.sort()
for x in total:
    print(x)

