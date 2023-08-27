'''
1번 backtracking을 쓰겠다
2번 포지션별 나열을 통해 포지션별 오름차순으로 선택한다. (0이면 해당 포지션에서 뛸 수 없다.)
3번 이미 해당 포지션을 선택했는지, 해당 선수가 선택됐는지를 체크해야한다. 
4번 해당 포지션을 선택하지 않은 것으로 원복시켜줄 필요가 있다.
'''
import sys

def input():
    return sys.stdin.readline().rstrip()

def process(position_list):
    tmp = sorted(list(enumerate(position_list)), key=lambda x: -x[1])
    return tmp

test_case = int(input())

for _ in range(test_case):
    dp = []
    for _ in range(11):
        dp.append(list(map(int, input().split())))
    position_by_player = list(map(process, list(map(list, zip(*dp)))))

    visited_player = [0 for _ in range(11)]
    visited_position = [0 for _ in range(11)]

    def backtracking(pos):
        # 모든 포지션에 대한 선수 배치가 완료되었을 때
        if pos == 11:
            return sum(visited_position)
        max_value = 0
        for index, stats in position_by_player[pos]:
            if not visited_player[index] and stats > 0:
                visited_player[index] = stats
                visited_position[pos] = stats
                max_value = max(max_value, backtracking(pos + 1))
                visited_player[index] = 0
                visited_position[pos] = 0
        return max_value

    print(backtracking(0))
                






