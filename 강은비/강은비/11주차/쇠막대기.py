import sys

s=sys.stdin.readline().rstrip()
st=[]
cnt=0
for i in range(len(s)):
    if s[i]=="(":
        st.append(s[i])
    else:
        if i>=1 and s[i-1]=="(":  #레이저
            st.pop()
            cnt+=len(st)
        else:
            cnt+=1
            st.pop()
    print(cnt)
print(cnt)
            