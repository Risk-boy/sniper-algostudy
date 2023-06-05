import sys

num_student = int(sys.stdin.readline().rstrip())
students = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(num_student)]

num_candidate = 3

votes = [[0, 0, 0] for _ in range(num_candidate)]

for s in students:
    for i, v in enumerate(s):
        votes[i][0] += v
        
        if v == 3:
            votes[i][1] += 1
            
        if v == 2:
            votes[i][2] += 1

votes_sorted = sorted(votes, reverse=True)

if votes_sorted[0] == votes_sorted[1]:
    print(0, votes_sorted[0][0])
else:
    print(votes.index(votes_sorted[0]) + 1, votes_sorted[0][0])