# 구현

msg = input()
n = len(msg)

rc = []
for i in range(1, n+1):
    if (n%i==0) and (i<=n//i):
        rc += [(i, n//i)]

r = rc[-1][0]
c = rc[-1][1]

read = [msg[i::r] for i in range(c)]
print(''.join(read)[:n])