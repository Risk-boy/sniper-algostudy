import sys
input = sys.stdin.readline 


n, r, c = map(int, input().split())
answer = 0

while n != 0:
    n -= 1
    
	# 11시
    if r < 2 ** n and c < 2 ** n:
        continue
	# 1시
    elif r < 2 ** n and c >= 2 ** n: 
        answer += 2 ** (2 * n) * 1
        c -= 2 ** n
	# 7시
    elif r >= 2 ** n and c < 2 ** n: 
        answer += 2 ** (2 * n) * 2
        r -= 2 ** n
	# 5시    
    else:
        answer += 2 ** (2 * n) * 3
        r -= 2 ** n
        c -= 2 ** n

print(answer)