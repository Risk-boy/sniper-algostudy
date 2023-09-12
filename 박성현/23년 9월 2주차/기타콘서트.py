import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

guitars = []
for _ in range(n):
    name, song = input().split()
    song_bit = int(song.replace('Y', '1').replace('N', '0'), 2)
    guitars.append(song_bit)

# print(guitars)
maxBit = 0  # 연주할 수 있는 최대 곡의 수
result = float('inf')  # 필요한 기타의 개수

def dfs(idx, combined_bit, cnt):
    global maxBit, result

    if idx == n:
        played_songs = bin(combined_bit).count('1')
        if played_songs > maxBit:
            maxBit = played_songs
            result = cnt
        elif played_songs == maxBit:
            result = min(result, cnt)
        return

    # 현재 기타를 선택하지 않는 경우
    dfs(idx + 1, combined_bit, cnt)
    # 현재 기타를 선택하는 경우
    dfs(idx + 1, combined_bit | guitars[idx], cnt + 1)

dfs(0, 0, 0)

if maxBit == 0:
    print(-1)
else:
    print(result)