import sys 
def input():
    return sys.stdin.readline().rstrip()

from itertools import combinations

num, target = map(int, input().split())
data = sorted(list(map(int, input().split())), reverse=True)

cand_data = combinations(data, 3)
answer = 0
for d in cand_data:
    if sum(d) <= target:
        answer = max(answer, sum(d))

print(answer)
