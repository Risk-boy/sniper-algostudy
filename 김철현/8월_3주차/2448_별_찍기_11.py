import sys
input = sys.stdin.readline 


def solve(size, blank):
    result = []
    if size == 3:
        result.append(" " * 2 + "*" + " " * 2)
        result.append(" " + "*" + " " + "*" + " ")
        result.append("*" * 5)
        return result 
    
    
    temp = solve(size // 2, blank // 2)
    for x in temp:
        result.append(" " * blank  + x + " " * blank)
    for x in temp:
        result.append(x + " " + x)

    return result


n = int(input())
total = solve(n, n // 2)
print("\n".join(total))