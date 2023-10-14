import sys
input = sys.stdin.readline 
from collections import defaultdict


N, K = map(int, input().split())
arr = list(map(int, input().split()))
dict = defaultdict(int)
start = 0
end = 0
max_len = 0
while end < N:
    if dict[arr[end]] < K:
        if max_len < end - start + 1:
            max_len = end - start + 1
        dict[arr[end]] += 1
        end += 1
    else:
        while arr[start] != arr[end]:
            dict[arr[start]] -= 1
            start += 1
        dict[arr[start]] -= 1
        start += 1

print(max_len)