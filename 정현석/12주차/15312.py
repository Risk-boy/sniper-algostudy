import sys

hint = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

total_list = []

for i in range(len(a)):
    total_list.append(hint[ord(a[i]) - ord('A')])
    total_list.append(hint[ord(b[i]) - ord('A')])
    
while len(total_list) > 2:
    temp = []
    for i in range(len(total_list) - 1):
        temp.append((total_list[i] + total_list[i+1]) % 10)
    total_list = temp
    
print(*total_list, sep='')