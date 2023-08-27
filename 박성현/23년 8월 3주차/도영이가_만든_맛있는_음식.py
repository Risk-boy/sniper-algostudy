import sys 
from itertools import combinations

INF = int(10e9)

def input():
    return sys.stdin.readline().rstrip()

def calculate(ingredients):
    sour = 1
    bitter = 0
    for i in ingredients:
        sour *= i[0]
        bitter += i[1]
    return abs(sour-bitter)


N = int(input())
ingredient = []
for _ in range(N):
    a, b = map(int,input().split())
    ingredient.append([a,b])

result = INF

for i in range(1,len(ingredient)+1):
    recipe = combinations(ingredient, i)
    for j in recipe:
        result = min(result, calculate(j))

print(result)
