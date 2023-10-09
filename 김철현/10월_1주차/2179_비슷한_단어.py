import sys
input = sys.stdin.readline 


N = int(input())
ls = []
for i in range(N):
    ls.append((input().rstrip(), i))

arr = sorted(ls)
length = [0] * N
max_len = -1

for i in range(N - 1):
    word1 = arr[i][0]
    word2 = arr[i + 1][0]
    word1_idx = arr[i][1]
    word2_idx = arr[i + 1][1]
    cnt = 0
    for j in range(min(len(word1), len(word2))):
        if word1[j] == word2[j]:
            cnt += 1
        else:
            break

    if cnt > max_len:
        max_len = cnt
    
    length[word1_idx] = max(length[word1_idx], cnt)
    length[word2_idx] = max(length[word2_idx], cnt)

check = False
for i in range(N):
    if length[i] == max_len and not check:
        print(ls[i][0])
        common = ls[i][0][:max_len]
        check = True
    elif length[i] == max_len:
        if common == ls[i][0][:max_len]:
            print(ls[i][0])
            break