import sys

logs_len = 5

logs = list(map(int, sys.stdin.readline().rstrip().split()))
logs_bool = [False for _ in logs]

while not all(logs_bool):
    for i in range(logs_len - 1):
        if logs[i] > logs[i + 1]:
            temp = logs[i]
            logs[i] = logs[i + 1]
            logs[i + 1] = temp
            print(*logs)
        if logs[i] == i + 1:
            logs_bool[i] = True
            
    if logs[logs_len - 1] == logs_len:
        logs_bool[logs_len - 1] = True