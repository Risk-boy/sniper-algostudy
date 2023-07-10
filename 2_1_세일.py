import sys 
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
data = [int(input()) for _ in range(N)]

def solution(data:list):
    '''
    data 라는 리스트를 받아서, 만약 data의 길이가 2 이하면 그냥 그 묶음이 최소가격이고
    3 이상이면 data를 내림차순으로 정렬한 뒤, 최대한 3개짜리 묶음을 많이 만들어내면 된다. 그렇게 하면 인덱스 0,1, 3,4, 6,7,.... 의 값만 더하면 된다.
    '''
    if len(data)<=2:
        print(sum(data))
    else:
        data = sorted(data, reverse=True)
        length = len(data)
        price = 0
        for i in range(0,length,3):
            price += data[i]
            try:
                price += data[i+1]
            except:
                continue
    print(price)

solution(data)

