import sys
input = sys.stdin.readline 


def group(word):
    my_dict = {}
    for i in range(len(word)):
        if word[i] not in my_dict:
            my_dict.setdefault(word[i], 1)
        else:
            if i-1 >= 0 and word[i-1] != word[i]:
                my_dict[word[i]] += 1
    for value in my_dict.values():
        if value > 1:
            return 0
    return 1


n = int(input())
words = []
for _ in range(n):
    words.append(input())
ans = 0
for word in words:
    ans += group(word)
print(ans)
