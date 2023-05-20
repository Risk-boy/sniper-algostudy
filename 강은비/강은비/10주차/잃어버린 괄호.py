import sys

s=sys.stdin.readline().rstrip()
tmp=s.split('-')
first=sum(map(int, tmp.pop(0).split('+')))  #더하기로 묶인것들 다 더해주고 차례로 빼주기
for x in tmp:
    first-=sum(map(int, x.split('+')))
print(first)

'''
s=sys.stdin.readline().rstrip()
tmp=s.split('-')
first=sum(map(int, tmp.pop(0).split('+')))  #더하기로 묶인것들 다 더해주고 차례로 빼주기
print(first, tmp)
for x in tmp:
    first-=sum(map(int, x.split('+')))
print(first)


'''