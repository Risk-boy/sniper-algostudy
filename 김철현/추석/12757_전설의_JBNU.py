import sys
input = sys.stdin.readline 
from bisect import insort, bisect_left


def find_nearest_keys(key):
    idx = bisect_left(keys, key)
    if idx == 0:
        if keys[0] - key <= K:
            return [keys[0]]
    elif idx == len(keys):
        if key - keys[-1] <= K:
            return [keys[-1]]
    else:
        left_key = keys[idx - 1]
        right_key = keys[idx]
        if key - left_key < right_key - key:
            if key - left_key <= K:
                return [left_key]
        elif key - left_key > right_key - key:
            if right_key - key <= K:
                return [right_key]
        else:
            return [left_key, right_key]
    return []
            
N, M, K = map(int, input().split())
dict = dict()
keys = []
for _ in range(N):
    k, v = map(int, input().split())
    dict[k] = v
    insort(keys, k)

for _ in range(M):
    cmd, *items = map(int, input().split())
    if cmd == 1:
        dict[items[0]] = items[1]
        insort(keys, items[0])
    elif cmd == 2:
        v = dict.get(items[0], -1)
        if v != -1:
            dict[items[0]] = items[1]
        else:
            key = find_nearest_keys(items[0])
            if len(key) == 1:
                dict[key[0]] = items[1]
    elif cmd == 3:
        v = dict.get(items[0], -1)
        if v != -1:
            print(v)
        else:
            key = find_nearest_keys(items[0])
            if len(key) == 0:
                print(-1)
            elif len(key) == 2:
                print("?")
            else:
                print(dict[key[0]])