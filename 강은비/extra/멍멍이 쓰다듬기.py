import sys

monkey, dog = map(int, sys.stdin.readline().split())
dog -= monkey
if dog <= 1:
    print(dog)
else:
    idx = 0
    for i in range(1, dog):
        idx += i
        if dog <= idx:
            print(2 * i - 1)
            break
        idx += i
        if dog <= idx:
            print(2 * i)
            break