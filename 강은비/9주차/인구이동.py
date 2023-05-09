import sys
from collections import deque

def check(x, y):
    dx=[0, -1, 0, 1]
    dy=[-1, 0, 1, 0]
    q=deque([(x, y)])
    u=set()
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
                if l<=abs(a[x][y]-a[nx][ny])<=r:
                    q.append((nx, ny))
                    visit[nx][ny]=1
                    u.add((nx, ny))
    return u

def unite():
    for u in tu:
        total=sum([a[x][y] for x, y in u])
        for x, y in u:
            a[x][y]=total//len(u)

n, l, r=map(int, sys.stdin.readline().split())
a=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt=0
while True:
    visit=[[0 for _ in range(n)] for _ in range(n)]
    flag=False
    tu=[]
    for x in range(n):
        for y in range(n):
            u=check(x, y)
            if u:
                flag=True
                u.add((x,y))
                tu.append(u)
    unite()
    if not flag:
        print(cnt)
        break
    cnt+=1