import sys 
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
INF = int(10e9)

synergy = [list(map(int,input().split())) for _ in range(N)]

from itertools import combinations, permutations

def team_synergy(teams):
    '''
    [1,2,3,4]라는 team원들이 결정되었을 때, 4C2의 조합을 구해서 시너지들을 더하기
    '''
    score = 0
    for c in combinations(teams, 2):
        i,j = c 
        score += synergy[i-1][j-1]
        score += synergy[j-1][i-1]
    return score

result = INF
player_list = range(1,N+1)
for c in combinations(range(1,N+1), N//2):
    team_a, team_b = team_synergy(c), team_synergy(list(set(player_list)-set(c)))
    result = min(result, abs(team_b-team_a))

print(result)





