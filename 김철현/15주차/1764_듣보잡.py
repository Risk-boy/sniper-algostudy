import sys
input = sys.stdin.readline 


n, m = map(int, input().split())

dict = {}
for _ in range(n + m):
    name = input().rstrip()
    if name not in dict:
        dict.setdefault(name, 1)
    else:
        dict[name] += 1

ls = list()
for key in dict.keys():
    if dict[key] == 2:
        ls.append(key)

ls.sort()
print(len(ls))
for name in ls:
    print(name)