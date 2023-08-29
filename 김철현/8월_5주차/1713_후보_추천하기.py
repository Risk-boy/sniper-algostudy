import sys
input = sys.stdin.readline 


n = int(input())
m = int(input())
arr = list(map(int, input().split()))
ls = [[0, 0] for _ in range(101)]
cnt = 0
for i in range(m):
    if cnt < n:
        if not ls[arr[i]][0]:
            cnt += 1
            ls[arr[i]][0] += 1
            ls[arr[i]][1] = i
        else:
            ls[arr[i]][0] += 1
    else:
        if ls[arr[i]][0]:
            ls[arr[i]][0] += 1
        else:
            min_cnt = m + 1
            old_idx = m + 1
            idx = -1
            for j in range(1, 101):
                if ls[j][0]:
                    if ls[j][0] < min_cnt:
                        min_cnt = ls[j][0]
                        idx = j
                        old_idx = ls[j][1]
                    elif ls[j][0] == min_cnt:
                        if ls[j][1] < old_idx:
                            old_idx = ls[j][1]
                            idx = j
            ls[idx][0] = 0
            ls[idx][1] = 0
            ls[arr[i]][0] += 1
            ls[arr[i]][1] = i


for i in range(101):
    if ls[i][0]:
        print(i, end=" ")

