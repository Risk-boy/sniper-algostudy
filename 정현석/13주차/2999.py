import sys
import math

message = sys.stdin.readline().rstrip()

len_message = len(message)

r = int(math.sqrt(len_message))

while len_message % r:
    r -= 1
    
c = len_message // r
    
encoding_matrix = [message[i:i+r] for i in range(0, len_message, r)]

for i in range(r):
    for j in range(c):
        print(encoding_matrix[j][i], end='')