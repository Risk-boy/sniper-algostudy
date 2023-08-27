import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
total = [int(input()) for _ in range(N)]

# N개를 M묶음으로 나눌건데, 이 나누는 경우는... 너무 많다. 이진탐색?
# N일동안의 데이터 중 최대로 해보고 성공하면 반을 줄여보고, 그런식으로 해볼까? 한 번 금액은 10000원이 최대이니까

def is_possible(mid):
    count = 1
    remaining = mid
    for i in range(N):
        if remaining >= total[i]:
            remaining -= total[i]
        else:
            count += 1
            remaining = mid - total[i]
    return count <= M

def money_withdrawl():
    start = max(max(total), sum(total)//M)
    last = sum(total)
    answer = last

    while start <= last:
        mid = (start + last)//2
        if is_possible(mid):
            answer = mid
            last = mid - 1 
        else:
            start = mid + 1 
    return answer

print(money_withdrawl())




