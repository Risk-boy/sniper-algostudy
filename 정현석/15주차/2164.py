import sys

num_cards = int(sys.stdin.readline().rstrip())
deck = [i for i in range(1, num_cards+1)]

while num_cards > 1:
    deck = deck[1::2]
    
    if num_cards & 1:
        deck.append(deck.pop(0))
        
    num_cards //= 2

print(*deck)