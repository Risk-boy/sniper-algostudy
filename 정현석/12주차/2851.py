import sys

mushrooms_len = 10

mushrooms = [int(sys.stdin.readline().rstrip()) for _ in range(mushrooms_len)]

result = 0

for i in range(mushrooms_len):
    result += mushrooms[i]
    
    if result >= 100:
        break
    
if abs(result - 100) <= abs(result - mushrooms[i] - 100):
    print(result)
else:
    print(result - mushrooms[i])