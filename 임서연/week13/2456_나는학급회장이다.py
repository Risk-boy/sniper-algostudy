# 구현

import sys

n = int(input())
fir, sec, thr = [], [], []
for i in range(n):
    f, s, t = map(int, sys.stdin.readline().split())
    fir += [f]
    sec += [s]
    thr += [t]

canditate_fir = [sum(fir), fir.count(3)]
canditate_sec = [sum(sec), sec.count(3)]
canditate_thr = [sum(thr), thr.count(3)]

best = 0
score = 0
cnt = 0
for i, result in enumerate([canditate_fir, canditate_sec, canditate_thr]):
    if result[0] > score:
        score = result[0]
        cnt = result[1]
        best = i+1
    elif result[0] == score:
        if result[1] > cnt:
            score = result[0]
            cnt = result[1]
            best = i+1
        elif result[1] == cnt:
            score = result[0]
            best = 0

print(best, score)