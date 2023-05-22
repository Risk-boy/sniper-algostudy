import sys

exp = sys.stdin.readline().rstrip()

exp_minus = exp.split('-')

exp_minus_plus = [sum(list(map(int, e.split('+')))) for e in exp_minus]

first = exp_minus_plus.pop(0)

print(first - sum(exp_minus_plus))