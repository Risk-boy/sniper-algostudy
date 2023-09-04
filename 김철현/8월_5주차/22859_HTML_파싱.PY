import sys
input = sys.stdin.readline 


s = input().rstrip()[6:-7]
n = len(s)
i = 0
while i < n - 5:
    if s[i] == "<":
        if s[i + 1] == "d":
            title = ""
            while s[i] != '"':
                i += 1
            i += 1
            while s[i] != '"':
                title += s[i]
                i += 1
            print(f"title : {title}")
        elif s[i + 1] == "p":
            i += 3
            sentence = ""
            while s[i:i+4] != "</p>":
                if s[i] == "<":
                    while s[i] != ">":
                        i += 1
                elif s[i] == " ":
                    if sentence and sentence[-1] != " ":
                        sentence += " "
                else:
                    sentence += s[i]
                i += 1
            print(sentence)
    i += 1
