import sys
from collections import deque

n=int(sys.stdin.readline())
cards=deque(range(1, n+1))

while len(cards)>=2:
    cards.popleft() 
    cards.rotate(-1)    

print(cards[0])