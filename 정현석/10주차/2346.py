import sys

n = int(sys.stdin.readline().rstrip())
notes = list(map(int, sys.stdin.readline().rstrip().split()))
balloons = list(range(n))

result = []

index = 0
while True:
    result.append(balloons[index] + 1)
    note = notes[balloons.pop(index)]
    
    if not balloons:
        break
    
    if note > 0:
        index -= 1
    
    index += note
    index %= len(balloons)
    
print(*result)