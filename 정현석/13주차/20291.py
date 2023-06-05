import sys

n = int(sys.stdin.readline().rstrip())
files = [sys.stdin.readline().rstrip() for _ in range(n)]

files_dict = {}

for f in files:
    extension = f.split('.')[-1]
    if extension not in files_dict:
        files_dict[extension] = 1
    else:
        files_dict[extension] += 1
        
for e in sorted(files_dict.keys()):
    print(e, files_dict[e])