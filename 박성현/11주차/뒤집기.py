from collections import deque, Counter, defaultdict
q = deque(list(map(int,list(input()))))
temp_1 = [q[0]]
start = q[0]
while q:
    a = q.popleft()
    if start == a :
        continue
    else:
        start = a
        temp_1.append(a)
        
X = Counter(temp_1)
if len(X.keys())==1:
    print(0)
else:
    print(min(X[0], X[1]))