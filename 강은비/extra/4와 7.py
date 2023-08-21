import sys

k = int(sys.stdin.readline())
n = 0
i = 1
answer = ""

while True:
    if n+2**i>=k:  # i 는 n의 자리 수
        k-= n+1
        break
    n += 2**i
    i += 1
    
while i>=1:
    if k<2**(i-1):
        answer+="4"
    else:
        answer+="7"
        k-=2**(i-1)
    i-=1
print(answer)
   