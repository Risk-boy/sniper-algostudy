length = int(input().rstrip())
data = list(map(int,input().rstrip().split()))
check = [False]*length

tmp = []
start = [data[0]]
for i in data[1:]:
    #print("i: ", i, "start: ", start)
    # 내리막길인 경우
    if i < start[-1]:
        tmp.append(start)
        start = [i]
    # 평지인 경우
    elif i == start[-1]:
        tmp.append(start)
        start = [i]
    else:
        start.append(i)
tmp.append(start)
result = []
for i in tmp:
    if len(i)>=2:
        result.append(i[-1]-i[0])
#print(tmp, result)
if len(result)==0:
    print(0)
else:
    print(max(result))


    