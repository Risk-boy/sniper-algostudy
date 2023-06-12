import sys

[n, m] = list(map(int, sys.stdin.readline().rstrip().split()))
paint = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

count = 0

for p in paint:
    seqs = ''.join(map(str,p)).split('0')
    
    for seq in seqs:
        if not seq:
            continue
        
        seq_count = 1
        prev = seq[0]
        for c in seq[1:]:
            if c != prev:
                seq_count += 1
            prev = c
            
        count += seq_count // 2 + 1

print(count)