# 다이나믹 프로그래밍


# import sys
# import itertools

# t = int(input())

# for _ in range(t):
#     n = int(sys.stdin.readline().strip())
    
#     cnt = 0
#     for i in range(n//3+1):
#         for j in range(n//2+1):
#             if (3*i+2*j)<=n:
#                 k = n - 3*i - 2*j
#                 kinds = i+j+k
#                 comb_3 = len(list(itertools.combinations([0]*kinds, i)))
#                 comb_2 = len(list(itertools.combinations([0]*(kinds-i), j)))
#                 cnt += comb_3*comb_2
#     print(cnt)



import sys

t = int(input())

num = [0] * 12

num[1:4] = [1,2,4]

for i in range(4, len(num)):
    num[i] = num[i-3] + num[i-2] + num[i-1]

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(num[n])