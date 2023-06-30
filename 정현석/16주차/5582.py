import sys

seq1 = sys.stdin.readline().rstrip()
seq2 = sys.stdin.readline().rstrip()
seq1_len = len(seq1)
seq2_len = len(seq2)

if seq2_len < seq1_len:
    temp = seq1
    temp_len = seq1_len
    seq1 = seq2
    seq1_len = seq2_len
    seq2 = temp
    seq2_len = temp_len

max_len = 0

dp = [0 for _ in range(seq1_len+1)]

for i in range(1, seq1_len+1):
    for j in range(dp[i-1], -1, -1):
        if seq1[i-j-1:i] in seq2:
            dp[i] = j+1
            break
    
print(max(dp))