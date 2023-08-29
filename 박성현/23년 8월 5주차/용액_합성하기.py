import sys 
from itertools import combinations

INF = int(10e9)
N = int(input())
solution = list(map(int,input().split()))

left, right = 0, N-1 
min_sum = INF 

while left < right:
    cur_sum = solution[left] + solution[right]
    if abs(cur_sum) < abs(min_sum):
        min_sum = cur_sum
    if cur_sum > 0 :
        right -= 1 
    elif cur_sum < 0:
        left += 1
    else:
        break

print(min_sum)




