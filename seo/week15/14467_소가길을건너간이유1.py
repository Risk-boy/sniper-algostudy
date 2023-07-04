import sys

n = int(input())
cow_coor = {}
cow_cnt = [0]*10

for i in range(n):
    cow, coord = map(int, sys.stdin.readline().split())
    if (cow in cow_coor) and (cow_coor[cow]!=coord):
        cow_cnt[cow-1] += 1
        cow_coor[cow] = coord
    else:
        cow_coor[cow] = coord

print(sum(cow_cnt))