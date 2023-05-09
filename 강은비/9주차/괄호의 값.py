import sys

def check(y):
    k, ck=2, "("
    if y=="]":
        k, ck=3, "["
        
    n=1
    if st[-1].isdigit():
        n=0
        while st and st[-1].isdigit():
            n+=int(st.pop())
    if st and st[-1]==ck:
        st.pop() 
        st.append(str(k*n))
        return 1
    else:    #비정상
        return 0
        

s=sys.stdin.readline().strip()
st=[]
for x in s:
    if not st or x=="(" or x=="[":
        st.append(x)
    elif x==")" or x=="]":
        if not check(x):
            print(0)
            break
else:
    answer=0
    for x in st:
        if x.isdigit():
            answer+=int(x)
        else:
            print(0)
            break
    else:
        print(answer)
            