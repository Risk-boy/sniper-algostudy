# 수학
# 구현

k = int(input())
ans = bin(k+1)[3:].replace('0', '4').replace('1', '7')
print(ans)