import sys
input = sys.stdin.readline 


arr = [int(input()) for _ in range(10)]

answer = arr[0]

for i in range(1, 10):
    cur_sum = answer + arr[i]
    if abs(cur_sum - 100) < abs(answer - 100):
        answer = cur_sum

    elif abs(cur_sum - 100) == abs(answer - 100):
        if answer < cur_sum:
            answer = cur_sum 
    
    else:
        break
    

print(answer)