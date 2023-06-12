import sys

[n, m, k] = list(map(int, sys.stdin.readline().rstrip().split()))

greetings = [int(sys.stdin.readline().rstrip()) for _ in range(m)]
greetings = int(''.join(['1' if i in greetings else '0' for i in range(n-1, -1, -1)]), 2)

for _ in range(k):
    left = (greetings << 1) & ~(1 << n)
    if (1 << (n-1)) & greetings:
        left |= 1
    right = greetings >> 1
    if 1 & greetings:
        right |= (1 << n-1)           
    
    greetings = left ^ right
    
print(sum(list(map(int, list(bin(greetings)[2:])))))