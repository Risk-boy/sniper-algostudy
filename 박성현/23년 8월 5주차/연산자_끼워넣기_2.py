import sys
from itertools import product

N = int(input())
sequence = list(map(int, input().split()))
ops_count = list(map(int, input().split()))

min_val = float('inf')
max_val = float('-inf')

# 연산자 기능 정의
def operate(a, b, op):
    if op == 0: return a + b
    if op == 1: return a - b
    if op == 2: return a * b
    if op == 3: 
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def backtrack(idx, result):
    global min_val, max_val
    
    # 연산자를 모두 사용한 경우
    if idx == N-1:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    # 각 연산자에 대한 처리
    for i in range(4):
        if ops_count[i] > 0:
            ops_count[i] -= 1
            backtrack(idx + 1, operate(result, sequence[idx + 1], i))
            ops_count[i] += 1

backtrack(0, sequence[0])
print(max_val)
print(min_val)
