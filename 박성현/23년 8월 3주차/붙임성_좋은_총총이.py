from collections import defaultdict
import sys

def input():
    return sys.stdin.readline().rstrip() 

N = int(input())
target = 'ChongChong'
result = defaultdict(int)

dance = defaultdict(int)
dance[target] += 1 

for _ in range(N):
    A, B = input().split()
    if dance[A] >=1:
        dance[B] += 1 
    if dance[B] >=1:
        dance[A] += 1 

print(len([key for key in dance.keys() if dance[key]>=1]))
    
