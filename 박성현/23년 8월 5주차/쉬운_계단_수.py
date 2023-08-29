N = int(input())

cnt = 0

def sol(data):
    global cnt

    if len(data) == N:
        cnt += 1
        return

    last_num = data[-1] if data else -1  
    
    if last_num == 9:
        data.append(8)
        sol(data)
        data.pop()
    elif last_num == 0:
        data.append(1)
        sol(data)
        data.pop()
    elif last_num == -1:  
        for i in range(1, 10):
            data.append(i)
            sol(data)
            data.pop()
    else:
        data.append(last_num + 1)
        sol(data)
        data.pop()
        
        data.append(last_num - 1)
        sol(data)
        data.pop()

sol([])
print(cnt % 1000000000)






