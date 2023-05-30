import sys

first = sys.stdin.readline().rstrip().split()

n = int(first[0])
seq = first[1:]

while len(seq) < n:
    seq += sys.stdin.readline().rstrip().split()

seq = sorted([int(s[::-1]) for s in seq])

for s in seq:
    print(s)