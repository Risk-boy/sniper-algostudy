import sys
from collections import defaultdict

def check(s, t):
    cnt = 0
    for a, b in zip(s, t):
        if a == b:
            cnt += 1
        else:
            break
    return cnt
    
input = sys.stdin.readline
n = int(input())

prefix = defaultdict(list)
word = {}
for i in range(n):
    s = input().rstrip()
    
    if word.get(s, -1) >= 0 :
        continue
    
    word[s] = i
    
    pre = ""
    for x in s:
        pre += x
        prefix[pre].append(s)
        

prefix = sorted(prefix.items(), key = lambda x: len(x[0]), reverse = True)        
for k, v in prefix:
    if len(v) >= 2:
        print(v[0])
        print(v[1])
        break
else:
    t = word.keys()
    print(t[0])
    print(t[1])
    
