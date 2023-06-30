import sys
from datetime import date

n = int(sys.stdin.readline().rstrip())
students = []
for _ in range(n):
    [name, d, m, y] = sys.stdin.readline().rstrip().split()
    students.append((name, date(int(y), int(m), int(d))))

min_date = date.max
max_date = date.min

for s in students:
    if s[1] < min_date:
        min_date = s[1]
        min_name = s[0]
    if s[1] > max_date:
        max_date = s[1]
        max_name = s[0]
        
print(max_name)
print(min_name)