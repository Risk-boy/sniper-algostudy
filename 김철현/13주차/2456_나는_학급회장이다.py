import sys
input = sys.stdin.readline 


n = int(input())
dict = {"1": [0, 0, 0], "2": [0, 0, 0], "3": [0, 0, 0]}
score1 = score2 = score3 = 0

for _ in range(n):
    a, b, c = map(int, input().split())
    score1 += a 
    dict["1"][a - 1] += 1
    score2 += b
    dict["2"][b - 1] += 1
    score3 += c
    dict["3"][c - 1] += 1

arr = [[score1] + dict["1"] + ["1"], [score2] + dict["2"] + ["2"], [score3] + dict["3"] + ["3"]]
arr.sort(key=lambda x:(-x[0], -x[1], -x[2]))
if arr[0][1] != arr[1][1]:
    print(arr[0][4], arr[0][0])
else:
    if arr[0][2] != arr[1][2]:
        print(arr[0][4], arr[0][0])
    else:
        print(0, arr[0][0])
