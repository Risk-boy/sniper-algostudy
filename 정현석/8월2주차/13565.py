import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(m)]

end = m-1

def check():
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    s = []
    for i in range(n):
        if not board[0][i]:
            s.append((0, i))
            
    while s:
        r, c = s.pop()
        
        if r == end:
            return "YES"
        
        if board[r][c] != -1:
            board[r][c] = -1
            
            for dr, dc in directions:
                r_next = r + dr
                c_next = c + dc
                
                if r_next >= 0 and r_next < m and c_next >= 0 and c_next < n and not board[r_next][c_next]:
                    s.append((r_next, c_next))
    
    return "NO"

print(check())