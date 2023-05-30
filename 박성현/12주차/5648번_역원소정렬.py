import sys
def input():
    return sys.stdin.readline().rstrip()

start = input().split()
data = []
if len(start)==1:
    N = int(start)
else:
    N = int(start[0])
    for i in start[1:]:
        data.append(int(i[::-1]))


while len(data) != N:
    X = map(lambda x: int(x[::-1]), input().split())
    data.extend(X)

answer = sorted(data)
for i in answer:
    print(i)