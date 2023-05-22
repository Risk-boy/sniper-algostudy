import sys
input = sys.stdin.readline 


t = 0
while True:
    t += 1
    l, p, v = map(int, input().split())
    if l == 0:
        break
    
    answer = 0
    while v > 0:
        if l < v:
            answer += l
        else:
            answer += v
        v -= p
    print(f"Case {t}: {answer}")