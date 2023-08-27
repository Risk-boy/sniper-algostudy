from itertools import combinations
import random
import sys

people = [ '김', '강', '임', '정', '박' ]	# 사람 이름 적기
problems = sys.stdin.readline().split()		# 문제 입력 받음
assignments = {}

# 랜덤하게 2문제 풀 사람을 선택
two_problem_people = random.sample(people, len(problems)%len(people))
one_problem_people = [p for p in people if p not in two_problem_people]

# 문제를 섞어서 무작위로 정렬
random.shuffle(problems)

# 2문제 풀 사람에게 문제 할당
for person in two_problem_people:
	assignments[person] = [problems.pop(), problems.pop()]

# 나머지 사람들에게 1문제 할당
for person in one_problem_people:
	assignments[person] = [problems.pop()]

# 결과 출력
for person, assigned_problems in assignments.items():
	print(f"{person}: {assigned_problems}")