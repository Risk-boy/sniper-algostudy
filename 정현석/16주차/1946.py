import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    
    applicants = sorted([list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)])
    
    max_applicants = 1
    min_score = applicants[0][1]
    
    for i in range(1, n):
        if applicants[i][1] < min_score:
            min_score = applicants[i][1]
            max_applicants += 1
    
    print(max_applicants)