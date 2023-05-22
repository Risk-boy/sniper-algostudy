import sys
input = sys.stdin.readline 


n, r, c = map(int, input().split())
answer = 0

while n != 0:
    n -= 1
    
	# 1사분면
    if r < 2 ** n and c < 2 ** n:
        continue
	# 2사분면
    elif r < 2 ** n and c >= 2 ** n: 
        answer += 2 ** (2 * n) * 1
        c -= 2 ** n
	# 3사분면
    elif r >= 2 ** n and c < 2 ** n: 
        answer += 2 ** (2 * n) * 2
        r -= 2 ** n
	# 4사분면    
    else:
        answer += 2 ** (2 * n) * 3
        r -= 2 ** n
        c -= 2 ** n

print(answer)