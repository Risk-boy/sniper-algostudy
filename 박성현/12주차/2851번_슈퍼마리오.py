# import sys
# input = sys.stdin.readline

# 데이터 입력으로 받음
data = []
for _ in range(10):
    data.append(int(input().rstrip()))


answer = 0 
for d in data:
    answer += d 
    if answer >= 100 :
        if answer-100 > 100-(answer-d):
            answer -= d 
        break
print(answer)

    




