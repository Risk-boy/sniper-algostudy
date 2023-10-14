import sys
input = sys.stdin.readline 


def change(x):
    if x < 10:
        x = "0" + str(x)
    return x


N = int(input())
arr = []
for _ in range(N):
    team, time = input().rstrip().split()
    arr.append((int(time[:2]), int(time[3:]), int(team)))


t1 = 0
t2 = 0
score1 = 0
score2 = 0
cur_m = 0
cur_s = 0
for m, s, t in arr:
    if score1 > score2:
        if cur_s <= s:
            t1 += (60 * (m - cur_m) + s - cur_s)
        else:
            t1 += (60 * (m - cur_m - 1) + 60 - cur_s + s)
    elif score2 > score1:
        if cur_s <= s:
            t2 += (60 * (m - cur_m) + s - cur_s)
        else:
            t2 += (60 * (m - cur_m - 1) + 60 - cur_s + s)
                
    if t == 1:
        score1 += 1
    else:
        score2 += 1
    
    cur_m = m
    cur_s = s

if score1 > score2:
    t1 += 60 * 48 - (60 * cur_m + cur_s)
elif score2 > score1:
    t2 += 60 * 48 - (60 * cur_m + cur_s)

m1, s1 = t1 // 60, t1 % 60
m2, s2 = t2 // 60, t2 % 60

m1, s1, m2, s2 = change(m1), change(s1), change(m2), change(s2)
print(f"{m1}:{s1}")
print(f"{m2}:{s2}")