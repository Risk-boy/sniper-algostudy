import sys

num_sum = int(sys.stdin.readline().rstrip())

count = 0

while num_sum >= 0:
    count += 1
    num_sum -= count
    
print(count - 1)