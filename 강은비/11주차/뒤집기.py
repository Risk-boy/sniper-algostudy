import sys

s=sys.stdin.readline().rstrip()
zero=[x for x in s.split("0") if x]
one=[x for x in s.split("1") if x]

print(len(zero)) if len(zero)<len(one) else print(len(one))