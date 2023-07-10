import sys

n = int(sys.stdin.readline().rstrip())

count = 0

for _ in range(n):
    word = list(sys.stdin.readline().rstrip())
    
    flag = True
    
    letters = set()
    prev = None
    for i in range(len(word)):
        if prev != word[i]:
            if word[i] not in letters:
                letters.add(word[i])
            else:
                flag = False
                break
        prev = word[i]
    if flag:
        count += 1
    
print(count)