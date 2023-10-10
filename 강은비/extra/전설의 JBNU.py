import sys

def find(num):
    l = 0
    r = len(key) - 1
    while l <= r:
        mid = (l + r) // 2
        if key[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
            
    return l

def search(k):
    idx = find(k)
    if idx == 0 or idx == len(key):
        if idx:
            idx -= 1
        if abs(key[idx] - k) <= dist:
            return key[idx]
        
        return -1
    
    r = abs(key[idx] - k)
    l = abs(key[idx - 1] - k) 
    
    if l > dist and r > dist:
        return -1
    
    if l < r:
        return key[idx - 1]
    if l > r:
        return key[idx]
    
    return "?"

input = sys.stdin.readline
d = {}
key = []
n, m, dist = map(int, input().split())
for _ in range(n):
    k, v = map(int, input().split())
    d[k] = v
    key.append(k)
key.sort()

for _ in range(m):
    s = list(map(int, input().split()))
    if s[0] == 1:
       key.insert(find(s[1]), s[1])
       d[s[1]] = s[2]
       
    elif s[0] == 2:
        if d.get(s[1], -1) >= 0:
            d[s[1]] = s[2]
        else:
            res = search(s[1])
            if res == "?" or res == -1:
                continue
            d[res] = s[2]
        
    else:
        if d.get(s[1], -1) >= 0:
            print(d[s[1]])
        else:
            res = search(s[1])
            print(res if res == "?" or res == -1 else d[res])
