import sys

n = int(sys.stdin.readline())
meet = {"ChongChong"}
for _ in range(n):
    a, b = sys.stdin.readline().split()
    if a in meet:
        meet.add(b)
    elif b in meet:
        meet.add(a)
        
print(len(meet))
        