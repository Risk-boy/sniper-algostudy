import sys

s = sys.stdin.readline().rstrip()

if "_" in s and s.islower():
    l = s.split("_")
    if "" in l:
        print("Error!")
    else:
        for i in range(1, len(l)):
            l[i] = l[i].title()
        print("".join(l))
        
elif s.isalpha() and s[0].islower():
    tmp = ""
    for x in s:
        if x.isupper():
            tmp +="_"+x.lower()
        else:
            tmp+=x
    print(tmp)
    
else:
    print( "Error!")