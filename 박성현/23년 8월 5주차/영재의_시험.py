import sys 

sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip()

answer = list(map(int,input().split()))
cnt = 0

def sol(ind, score, prev1, prev2):
    global cnt, answer
    
    # 만약 남은 문제수와 현재 점수를 확인해 어떻게 해도 5점을 넘지 못한다면 중단
    if score + (10 - ind) < 5:
        return

    # 10개의 답을 다 찍은 시점에
    if ind == 10:
        # 5점 이상이면 cnt += 1 
        if score >= 5:
            cnt += 1
        return 

    for i in range(1, 6):
        # 세 개의 값이 연속인지 확인
        if prev1 == prev2 == i:
            continue

        new_score = score + (answer[ind] == i)
        sol(ind+1, new_score, prev2, i)

sol(0, 0, 0, 0)  # 어차피 prev1, prev2는 0으로 설정해도 됨. 답은 1~6 사이의 값이므로.
print(cnt)