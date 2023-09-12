import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

def get_count_dict(numbers):
    count_dict = defaultdict(int)
    for num in numbers:
        count_dict[num] += 1
    return count_dict

N = int(input())
initial_balls = list(map(int, input().split()))
ball_count = get_count_dict(initial_balls)

Q = int(input())

for _ in range(Q):
    A = list(map(int, input().split()))[1:]
    count_A = get_count_dict(A)
    
    is_possible = all(ball_count[a] >= v for a, v in count_A.items())

    B = list(map(int, input().split()))[1:]
    count_B = get_count_dict(B)

    if is_possible:
        for a, v in count_A.items():
            ball_count[a] -= v
        for b, v in count_B.items():
            ball_count[b] += v

result = [ball for ball, count in ball_count.items() for _ in range(count)]
print(len(result))
if result:
    print(*result)