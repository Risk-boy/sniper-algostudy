import sys 
import re 

def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b

def solve(expression, index, current_value):
    if index == len(expression):
        return current_value

    # 괄호 없이 계산하는 경우
    no_bracket = calculate(current_value, expression[index], expression[index + 1])

    # 만약 현재 위치에서 괄호를 칠 수 있으면 괄호를 쳐서 계산
    if index + 2 < len(expression):
        in_bracket = calculate(expression[index + 1], expression[index + 2], expression[index + 3])
        with_bracket = calculate(current_value, expression[index], in_bracket)
        return max(solve(expression, index + 4, with_bracket), solve(expression, index + 2, no_bracket))
    
    # 괄호를 칠 수 없으면 괄호 없이 계산한 값만 리턴
    return solve(expression, index + 2, no_bracket)

N = int(input())
expression = input()
parsed_expression = [int(expression[0])]

for i in range(1, len(expression), 2):
    parsed_expression.append(expression[i])
    parsed_expression.append(int(expression[i+1]))
print(parsed_expression)

print(solve(parsed_expression, 1, parsed_expression[0]))