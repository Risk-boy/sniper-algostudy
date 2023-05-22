import sys

count = 1

while True:
    [l, p, v] = list(map(int, sys.stdin.readline().rstrip().split()))
    
    if l == 0:
        break
    
    q, r = divmod(v, p)
    
    result = q * l
    result += r if r < l else l
    
    print(f'Case {count}: {result}')
    count += 1