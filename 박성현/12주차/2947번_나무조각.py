def sol(data:list) -> None :  
    for i in range(4):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
            print(*data)
    if data != list(range(1,6)):
        sol(data)

data = list(map(int,input().rstrip().split()))
sol(data)