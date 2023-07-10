# 수학
# 구현

import sys
import collections

num = []
for i in range(10):
    num.append(int(input()))

mean = int(sum(num)/len(num))
num_dict = collections.Counter(num)
mode = num_dict.most_common(1)[0][0]

print(mean, mode, end='\n')