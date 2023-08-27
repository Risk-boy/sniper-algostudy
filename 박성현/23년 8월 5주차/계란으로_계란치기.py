import sys

def input():
    return sys.stdin.readline().rstrip()    

num_egg = int(input())
egg_list = [list(map(int, input().split())) for _ in range(num_egg)]

def solution(start):
    global max_break
    # 모든 계란을 확인했을 때
    if start == num_egg:
        cnt = 0
        for durability, _ in egg_list:
            if durability <= 0:
                cnt += 1
        max_break = max(max_break, cnt)
        return
    
    # 현재 계란이 깨져있으면 다음 계란을 선택
    if egg_list[start][0] <= 0:
        solution(start + 1)
        return
    
    is_broken = False
    for i in range(num_egg):
        # 자기 자신을 치거나, 이미 깨진 계란을 칠 필요는 없다
        if i == start or egg_list[i][0] <= 0:
            continue
        
        egg_list[start][0] -= egg_list[i][1]
        egg_list[i][0] -= egg_list[start][1]
        is_broken = True
        
        solution(start + 1)
        
        # 계란 상태 원복
        egg_list[start][0] += egg_list[i][1]
        egg_list[i][0] += egg_list[start][1]
    
    # 어떠한 계란도 칠 수 없는 경우
    if not is_broken:
        solution(start + 1)
    
max_break = 0
solution(0)
print(max_break)

# 들었던 계란으로 쳤는지 안쳤는지
# 원복을 했는지 안했는지