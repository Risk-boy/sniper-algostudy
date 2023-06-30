import sys

n = int(sys.stdin.readline().rstrip())

paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
counter = [0] * 3

def check_identity(rs, re, cs, ce):
    first = paper[rs][cs]
    
    for i in range(rs, re):
        for j in range(cs, ce):
            if first != paper[i][j]:
                return False
                
    return True

def find_papers(rs, re, cs, ce):
    
    if check_identity(rs, re, cs, ce):
        counter[paper[rs][cs] + 1] += 1
    else:        
        divisor_row = (re - rs) // 3
        divisor_col = (ce - cs) // 3
        
        for i in range(rs, re, divisor_row):
            for j in range(cs, ce, divisor_col):
                find_papers(i, i + divisor_row, j, j + divisor_col)
    
find_papers(0, n, 0, n)
print(*counter, sep = '\n')