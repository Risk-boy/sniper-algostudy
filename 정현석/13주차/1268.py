import sys

num_student = int(sys.stdin.readline().rstrip())
num_year = 5

students = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num_student)]
years = [[students[i][j] for i in range(num_student)] for j in range(num_year)]

friends = [set() for _ in range(num_student)]

for y in years:
    student_group = {}
        
    for i, c in enumerate(y):
        if c not in student_group:
            student_group[c] = set()
        else:
            student_group[c].add(i)
    
    for g in student_group.values():
        for s in g:
            friends[s] |= g
    
friends = [len(f) for f in friends]
print(friends.index(max(friends)) + 1)