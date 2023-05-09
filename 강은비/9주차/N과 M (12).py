import sys

def make(s, idx):   #비내림차순 순열 생성
    if len(s)==m:
        answer.append(s.copy())
        return 
    for i, x in enumerate(nums[idx:], idx):  #전에 삽입된 수 이상일때 append
        s.append(x)
        make(s, i)
        s.pop()
        
answer=[]
n, m=map(int, sys.stdin.readline().split())
nums=list(set(map(int, sys.stdin.readline().split()))) #중복제거 후 정렬
nums.sort()

make([], 0)
for row in answer:
    print(*row)