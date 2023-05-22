import sys
import itertools

[n, m] = list(map(int, sys.stdin.readline().rstrip().split()))

nums = list(map(int, sys.stdin.readline().rstrip().split()))
nums_set = set(nums)

sorted_perm = sorted([sorted(list(p)) for p in itertools.combinations_with_replacement(nums_set, m)])

for p in sorted_perm:
    print(' '.join(list(map(str,p))))