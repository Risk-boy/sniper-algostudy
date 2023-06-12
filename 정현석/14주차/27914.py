import sys

[n, k, q] = list(map(int, sys.stdin.readline().rstrip().split()))
students = list(map(int, sys.stdin.readline().rstrip().split()))
questions = list(map(int, sys.stdin.readline().rstrip().split()))

cases = [0] * n
longest = 0

if students[0] != k:
    cases[0] = 1
    longest = 1

for i in range(1, n):
    if students[i] == k:
        longest = 0
        cases[i] = cases[i-1]
    else:
        longest += 1
        cases[i] = cases[i-1] + longest

for q in questions:
    print(cases[q-1])