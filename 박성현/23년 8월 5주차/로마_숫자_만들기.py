import sys 
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

def sol(value, result):
    if value == N:
        return result
    new_result = []
    for x in result:
        new_result.extend([x+1, x+5, x+10, x+50])
    return sol(value+1, list(set(new_result)))

print(len(sol(0, [0])))

    