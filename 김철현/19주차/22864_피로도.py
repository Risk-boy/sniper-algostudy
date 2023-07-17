import sys
input = sys.stdin.readline 

""" 
a: 쌓이는 피로도
b: 처리가능한 일의 양
c: 1시간 쉬면 줄어드는 피로도
d: 최대 피로도
하루는 24시간
"""
a, b, c, m = map(int, input().split())
tired = 0
work = 0
time = 0
for i in range(1, 25):
    if tired + a <= m:
        tired += a
        work += b
        time += 1
    else:
        tired -= c
        if tired < 0:
            tired = 0
print(time * b)